import paramiko

host_name = '10.76.155.146'
u_name ='collectorlogin'
p_word = 'Cisco@321'
port_no = 22
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(host_name, username=u_name, password=p_word, port=port_no)
except paramiko.AuthenticationException:
    print("Authentication failed, please verify your credentials")

## To establesh sftp connection 
ftp = ssh.open_sftp()

## Copy file from remote machine to local 
#ftp.get('/home/collectorlogin/sriram/today.py', r'C:\Users\smellamp\Desktop\Sprint\today.py')

## Copy file from local machine to remote machine
src = r'C:\Users\smellamp\Desktop\Sprint\ok.txt'
rdst = '/home/collectorlogin/sriram/NOTE.py'

ftp.put(src, rdst)

ftp.close()
ssh.close()

