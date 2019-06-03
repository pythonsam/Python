import paramiko

host_name = '10.76.155.146'
u_name ='collectorlogin'
p_word = 'Cisco@321'
port_no = 22

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(host_name, username=u_name, password=p_word, port=port_no)

# To execute a command 
stdin, stdout, stderr = ssh.exec_command('ls /home/collectorlogin/srirkjam/')

#stdin, stdout, stderr = ssh.exec_command('touch /home/collectorlogin/sriram/local_new.py')

print(' stdout is ::', stdout.readlines())
print(' stderror is ::', stderr.read())

ssh.close()



