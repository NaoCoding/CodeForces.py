import requests
import json

def FutureContests() -> list:
    r = []
    a = json.loads(requests.get("https://codeforces.com/api/contest.list?gym=false").content.decode())
    if a['status'] == 'OK':
        for i in a['result']:
            if i['phase'] == "BEFORE":
                r.append(i['name'])
    r.reverse()
    return r


