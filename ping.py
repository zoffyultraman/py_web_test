import os
import paramiko
import re

client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('116.89.251.15',22,username='root',password='wpf960514',timeout=4)
stdin,stdout,stderr=client.exec_command('ping -c 1 103.74.172.207')
r=stdout.read()
print(r)
rq=(re.search('time='),r())
client.close