import requests
URL = "http://localhost:9000/servicelcm/service/deploymentStatus"
req = {
	'serviceid' : '11',
}		
requests.post(url = URL, json = req)			