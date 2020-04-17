import paramiko
import os
import time

def checkforError(stdout,stderr):	
	lines = stdout.readlines()
	if len(lines) != 0:
		print(lines[0])
		return
	lines = stderr.readlines()
	if len(lines) != 0:
		print("Error")
		print(lines[0])


def deployService(machine_username,machine_password,ip,port,serviceid, servicename,filepath, filename,sensor_topic):

	ssh_client =paramiko.SSHClient()
	ssh_client.load_system_host_keys()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=ip,username=machine_username,password=machine_password)


	stdin,stdout,stderr=ssh_client.exec_command("mkdir '"+serviceid+"'")	
	stdin,stdout,stderr=ssh_client.exec_command("chmod 777 '"+serviceid+"'")	
	ftp_client=ssh_client.open_sftp()
	ftp_client.put(filepath, './'+serviceid+'/'+filename)
	time.sleep(0.5)
	ftp_client.put('dockerfile', './'+serviceid+'/dockerfile')
	time.sleep(0.5)
	ftp_client.close()
	image_name = servicename + '_image '
	stdin,stdout,stderr=ssh_client.exec_command('echo root | sudo -S docker build -t ' + image_name + " '" + serviceid +"'")
	checkforError(stdout,stderr)
	# print(stderr.readlines())
	container_name = servicename + '_container'
	stdin,stdout,stderr=ssh_client.exec_command("echo root | sudo -S docker run -d --network='host' --name=" +container_name +' '+image_name)
	checkforError(stdout,stderr)
	# print(stdout.readlines())
	stdin,stdout,stderr=ssh_client.exec_command("echo root | sudo -S docker ps -aqf 'name="+ container_name+"'")
	print("Contaier id is ")
	lines = stdout.readlines()
	conid = lines[0]
	print(conid)
	return conid


