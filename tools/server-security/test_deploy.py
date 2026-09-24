import os
import pathlib
import shutil
import subprocess
import tempfile
import unittest

REQUIRED = 'index.html 404.html robots.txt tap/index.html tap/manual/index.html water/index.html apps/index.html projects/index.html'.split()

class DeploymentTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='deploy-tests-')
        self.root = pathlib.Path(self.temp.name)
        self.site = self.root / 'site with spaces'
        self.site.mkdir()
        script = pathlib.Path(os.environ.get('DEPLOY_TEST_SCRIPT', pathlib.Path(__file__).resolve().parents[2] / 'deploy_7iii.sh'))
        shutil.copy2(script, self.site / 'deploy_7iii.sh')
        key = self.root / 'test key'
        key.touch()
        (self.site / 'deploy_config.sh').write_text('DEPLOY_HOST=46.225.71.191\nDEPLOY_USER=simxn\nDEPLOY_REMOTE_PATH=/var/www/project7iii.com\nDEPLOY_SSH_KEY="' + str(key) + '"\n')
        self.bin = self.root / 'bin'
        self.bin.mkdir()
        fake_zola = '''#!/usr/bin/python3
import os, pathlib, sys
if os.environ.get('BUILD_MODE') == 'failure': sys.exit(9)
out = pathlib.Path(sys.argv[sys.argv.index('--output-dir') + 1])
for name in ''' + repr(REQUIRED) + ''':
    if os.environ.get('BUILD_MODE') == 'incomplete' and name == '404.html': continue
    target = out / name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text('built')
if os.environ.get('BUILD_MODE') == 'symlink': (out / 'unexpected').symlink_to('/etc/passwd')
'''
        fake_rsync = '''#!/usr/bin/python3
import json, os, pathlib, sys
pathlib.Path(os.environ['CALL_LOG']).write_text(json.dumps(sys.argv[1:]))
sys.exit(int(os.environ.get('RSYNC_EXIT', '0')))
'''
        fake_ssh = '''#!/usr/bin/python3
import os, pathlib
pathlib.Path(os.environ['SSH_LOG']).write_text('verified')
'''
        for name, content in [('zola', fake_zola), ('rsync', fake_rsync), ('ssh', fake_ssh)]:
            path = self.bin / name
            path.write_text(content)
            path.chmod(0o755)
        self.env = dict(os.environ, PATH=str(self.bin) + ':' + os.environ['PATH'], CALL_LOG=str(self.root / 'rsync.log'), SSH_LOG=str(self.root / 'ssh.log'))
    def tearDown(self):
        self.temp.cleanup()
    def run_deploy(self, *args, **extra):
        return subprocess.run(['bash', str(self.site / 'deploy_7iii.sh'), *args], cwd=self.root, env=dict(self.env, **extra), capture_output=True, text=True)
    def test_success_from_another_directory_and_paths_with_spaces(self):
        result = self.run_deploy()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.root / 'ssh.log').exists())
        import json
        arguments = json.loads((self.root / 'rsync.log').read_text())
        for option in ('--delay-updates', '--delete-delay', '--exclude=/foildata/'):
            self.assertIn(option, arguments)
        self.assertEqual(arguments[-1], 'simxn@46.225.71.191:/var/www/project7iii.com/')
    def test_dry_run_does_not_deploy_or_run_post_deploy_ssh(self):
        result = self.run_deploy('--dry-run')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('--dry-run', (self.root / 'rsync.log').read_text())
        self.assertFalse((self.root / 'ssh.log').exists())
    def test_invalid_build_never_contacts_server(self):
        for mode in ('failure', 'incomplete', 'symlink'):
            with self.subTest(mode=mode):
                self.assertNotEqual(self.run_deploy(BUILD_MODE=mode).returncode, 0)
                self.assertFalse((self.root / 'rsync.log').exists())
    def test_transfer_failure_is_not_success(self):
        self.assertEqual(self.run_deploy(RSYNC_EXIT='12').returncode, 12)
        self.assertFalse((self.root / 'ssh.log').exists())
    def test_unexpected_delete_target_is_rejected(self):
        config = self.site / 'deploy_config.sh'
        config.write_text(config.read_text().replace('/var/www/project7iii.com', '/var/www'))
        self.assertNotEqual(self.run_deploy().returncode, 0)
        self.assertFalse((self.root / 'rsync.log').exists())

if __name__ == '__main__':
    unittest.main()
