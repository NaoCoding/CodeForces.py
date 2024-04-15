import requests
import json

class user:

    def __init__(self,username):
        self.data = json.loads(requests.get("https://codeforces.com/api/user.info?handles="+username).content.decode())
        self.rating = self.data['result'][0]['rating']
        self.handle = self.data['result'][0]['handle']
        self.country = self.data['result'][0]['country']
        self.lastName = self.data['result'][0]['lastName']
        self.firstName = self.data['result'][0]['firstName']
        self.city = self.data['result'][0]['city']
        self.friendOfCount = self.data['result'][0]['friendOfCount']
        self.rank = self.data['result'][0]['rank']
        self.maxRating = self.data['result'][0]['maxRating']
        self.maxRank = self.data['result'][0]['maxRank']
        self.organization = self.data['result'][0]['organization']



