#Author: lisahoteng 2023/8/25
import paramiko
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
        ssh.connect(hostname=l[0], port=l[1], username=l[2], password=l[3])
    except Exception as e:
        print("host:"+l[0]+" connect fail!"+str(e))
        continue
    stdin, stdout, stderr = ssh.exec_command("df -h | sort |grep -E '/sd|/mapper' |awk '{print $1,$2,$3,$4,$5}'")
    print("host:"+l[0]+"\n",stdout.read().decode())
ssh.close()
pause=input("请按回车键或直接关闭窗口退出！")

