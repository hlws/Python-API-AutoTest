import paramiko
import os
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    f=open("hosts.txt","r")
except Exception as e:
    print("open file fail!"+str(e))
    exit(1)
for line in f.readlines():
    l=list(line.strip().split(":"))
    try:
        ssh.connect(hostname=l[0], port=l[1], username=l[2], password=l[3],timeout=60)
    except Exception as e:
        print("host:"+l[0]+" connect fail!"+str(e))
        # print(e)
        continue
    stdin, stdout, stderr = ssh.exec_command("df -Th")
    print("host:"+l[0]+"\n",stdout.read().decode())
ssh.close()

