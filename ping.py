import os
import paramiko
import re

client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('116.89.251.15',22,username='root',password='wpf960514',timeout=4)
stdin,stdout,stderr=client.exec_command('ping -c 1 103.74.172.207')
r=stdout.read()
print(r)
q1=(re.search(b'time=',r))
s1=str(q1)
print(s1)
time1=s1[24:27]
time2=s1[29:32]
ms1=int(time1)
ms2=int(time2)+7
print(r[ms1:ms2])
client.close