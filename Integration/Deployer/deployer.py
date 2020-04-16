import flask
import threading
import requests
import json
import sshclient
import deployer_helper
from flask import request


def req_handler(app,port):
	@app.route('/deploymentManager/deploy', methods=['POST'])
	def home():
		try :
			req = request.get_json()
			ip = req["serverip"]
			sshport = req['sshport']
			machine_username = req['machineusername']
			machine_password = req['password']
			serviceid = req['serviceid']
			username = req['username']
			application_name = req['applicationname']
			service_name = req['servicename']
			config_path = username + '/' + application_name + '/config.json'
			containerid = 12

			filename = deployer_helper.getFileName(config_path, service_name)			
			smres = deployer_helper.getSensorTopic(username,application_name,service_name,serviceid,config_path)
			deployer_helper.notifyActionManager(username,application_name,service_name,serviceid,config_path,smres['sensor_host'])
			sensortopic = smres['temporary_topic']			
			print("Returned Sensor topic by sensor manager is ",sensortopic)
			deployer_helper.generateDokerFile(config_path, service_name, sensortopic, serviceid)			
			file_path =  username + '/' + application_name + '/' + service_name + '/' + filename
			print("file path : ",file_path)			
			containerid = sshclient.deployService(machine_username, machine_password,ip,port,serviceid,service_name,file_path, filename,sensortopic)
			
			URL = "http://localhost:9000/servicelcm/service/deploymentStatus"
			req = {
				'serviceid' : serviceid,
				'username' : username,
				'status' : 'success',
				'serviceip' : ip,
				'sshport' : sshport,
				'containerid' : containerid
			}
			requests.post(url = URL, json = req)
			
		except Exception as error:
			print("Error ",error)
			URL = "http://localhost:9000/servicelcm/service/deploymentStatus"
			req = {
				'serviceid' : serviceid,
				'username' : username,
				'status' : 'fail',
				'serviceip' : ip,
				'sshport' : sshport,
				'containerid' : 'NULL'
			}		
			requests.post(url = URL, json = req)			
		res = {'status' : 'ok'}
		return flask.jsonify(res)

	app.run(port = port)

def main():
	app = flask.Flask('Deoployment Manger')
	port = 5050 #deployer port
	req_t = threading.Thread(target = req_handler, args = (app,port))
	req_t.start()
	req_t.join()
	return

if __name__ == '__main__':
	main()