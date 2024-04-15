import requests
import json

def FutureContestsNames() -> list:
    r = []
    a = json.loads(requests.get("https://codeforces.com/api/contest.list?gym=false").content.decode())
    if a['status'] == 'OK':
        for i in a['result']:
            if i['phase'] == "BEFORE":
                r.append(i['name'])
    r.reverse()
    return r

def UserGeneral(username : str):
    a = json.loads(requests.get("https://codeforces.com/api/user.info?handles="+username).content.decode())
    return a['result']

def UserRating(username : str):
    a = json.loads(requests.get("https://codeforces.com/api/user.info?handles="+username).content.decode())
    return a['result'][0]['rating']


