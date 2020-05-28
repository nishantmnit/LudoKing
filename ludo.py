import requests
import json
import time
import random

class ludo(object):
	def __init__(this):
		# 1 - down, 3 - up, 2 - 7
		this._burl 		= "https://misc-services.ludokingapi.com/api/v1/mini/7UpDown"
		this._schip 	= 10
		this._sloss 	= 1
		this._win 		= 0
		this._lcount 	= 0
		this._lbid 		= this._schip
		this._profile 	= this.setProfile()

	def createUrl(this):
		if this._lcount == 0:
			url = "%s/%s/%s" %(this._burl, this.getProfile(), this._schip)
		else:
			url = "%s/%s/%s*2" %(this._burl, this.getProfile(), this._lbid)
		return url

	def setProfile(this):
		choices = ["up", "down"]
		return random.choice(choices)

	def getProfile(this):
		if this._profile == "up":
			return 3
		else:
			return 1

	def sendReq(this):
		url = this.createUrl()
		auth_token="your game's bearer token"
		hed = {'Authorization': 'Bearer ' + auth_token}
		data = {'app' : 'aaaaa'}
		response = requests.get(url, json=data, headers=hed)
		this.parse(response.json())

	def _sprofile(this):
		this._profile = ("down" if this._profile == "up" else "up")

	def parse(this, data):
		y = data
		if ((y["2"] + y["1"] < 7) and this._profile == "down") or ((y["2"] + y["1"] > 7) and this._profile == "up"):
			this._win 		+= this._lbid
			this._lcount 	= 0
			this._lbid 		= this._schip
		else:
			this._win 		-= this._lbid
			this._lcount 	+= 1
			this._lbid 		= this._lbid * 2

		if int(y["nTotalChips"]) <= this._sloss:
			print "Total coins are less than %s. Exiting." %(this._sloss)
			quit()
		print "Total Wins = %s, Current coin count = %s, Next Bid = %s, bidding on = %s" %(this._win, y["nTotalChips"], this._lbid, this._profile)
		if this._win > 0:
			print "you won.. exiting."
			quit()

if __name__ == "__main__":
    obj = ludo()
    i = 0
    while i < 10:
    	obj.sendReq()
    	i+=1