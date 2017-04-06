#!/usr/bin/python

from paramiko.client import SSHClient

import paramiko

client = SSHClient()

client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

host = '192.168.202.8'
user = 'noturno'
password = '4linux'

client.connect(hostname=host, username=user, password=password)

