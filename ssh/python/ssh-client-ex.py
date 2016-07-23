#!/usr/bin/python

import paramiko, sys
from ssh_config import host, user, key_filename

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    client.connect(host, username=usern, key_filename=key_filename)
except Exception as e:
    print >> sys.stderr, "There was an exception connecting to the host: %s" % (e)
    client.close()
    sys.exit(1)
