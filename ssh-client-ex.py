#!/usr/bin/python

import paramiko
from ssh_config import config

c = config()

try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(c['host'], username=c['user'], key_filename=c['key_filename'])
except Exception as e:
    print "There was an exception connecting to the host: %s" % (e)
