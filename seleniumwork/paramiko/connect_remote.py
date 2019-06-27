import paramiko

host_name = '192.168.76.47'
u_name ='vixlive'
p_word = 'briter'
port_no = 22

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(host_name, username=u_name, password=p_word, port=port_no)

# To execute a command
stdin, stdout, stderr = ssh.exec_command('ls /usr2/shyamswork')

#stdin, stdout, stderr = ssh.exec_command('touch /data2/shyamswork/local_new.py')

print(' stdout is ::', stdout.readlines())
print(' stderror is ::', stderr.read())

ssh.close()
