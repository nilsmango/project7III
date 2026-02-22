#!/bin/bash
# sensitive info saved in the config
source deploy_config.sh

# SSH Deployment using rsync
rsync -rlvz --delete --exclude 'foildata' --no-perms --omit-dir-times -e "ssh -i $SSH_KEY" $LOCAL_PATH $USER@$HOST:$REMOTE_PATH

