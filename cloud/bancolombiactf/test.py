import os

os.environ['GIT_SSH_COMMAND'] = 'ssh -i /home/chan/practice/cloud/bancolombiactf/.ssh/id_rsa'
os.system('git ls-remote > reference')
