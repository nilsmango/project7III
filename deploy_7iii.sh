#!/bin/bash
# sensitive info saved in the config
source deploy_config.sh

# SSH Deployment using rsync
rsync -avz --delete --exclude 'foildata' -e "ssh -i $SSH_KEY" $LOCAL_PATH $USER@$HOST:$REMOTE_PATH

