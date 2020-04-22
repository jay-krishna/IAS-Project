import json
import requests


def auth(username,password):
    resp = dict()
    resp["username"] = username
    resp["password"] = password
    req = requests.post(url="http://0.0.0.0:5056/authlogin",data=json.dumps(resp))
    req = json.loads(req.text)
    if req["status"] == "failure":
        return False
    return True

def signup(username,password):
    resp = dict()
    resp["username"] = username
    resp["password"] = password
    req = requests.post(url="http://0.0.0.0:5056/authsignup",data=json.dumps(resp))
    req = json.loads(req.text)
    if req["status"] == "failure":
        return False
    return True
