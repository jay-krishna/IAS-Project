import requests
import json

def main():
	user_id = input('Enter User ID : ')
	data=None
	with open('./config.json') as f:
		data = json.load(f)
	# Make Request To Sensor Registration To Register the sensor 
	URL = "http://127.0.0.1:5060/"
	para = {'user_id' : user_id , 'config_file'=data}


	response = requests.post(url=URL, params = para).text
	# resp = response.json()
	# print(resp['msg'])
	
	
if __name__ == '__main__':
	main()