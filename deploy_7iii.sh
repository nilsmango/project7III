#!/bin/bash
# sensitive info saved in the config
source deploy_config.sh

# FTP Deployment using lftp
lftp -c "open -u $USER,$PASSWORD $HOST; mirror -R --delete --verbose --exclude 'foildata' $LOCAL_PATH $REMOTE_PATH"

