import requests
import json

# auth rocketchat
authdata = {"user": "xxxxx", "password": "yyyyy"}
authResponse = requests.post("http://zzzzz:3000/api/v1/login", data=authdata)

userId = json.loads(authResponse.text)['data']['userId']
authToken = json.loads(authResponse.text)['data']['authToken']
sendheaders = {"X-User-Id": userId, "X-Auth-Token": authToken}

# search room's info
room = {"roomName": "test-room"}
roomInfo = requests.get("http://zzzzz:3000/api/v1/rooms.info", params=room, headers=sendheaders)
print(roomInfo.text)