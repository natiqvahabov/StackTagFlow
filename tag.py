import requests
import json

tag = ""
tag = input("Enter tag: ")

if(tag==""):
	print("Enter valid tag")
else:
	api_url = "https://api.stackexchange.com/2.2/questions?order=desc&pagesize=5&sort=creation&tagged={}&site=stackoverflow".format(tag)
	r = requests.get(api_url).json()
	i=0

	if(len(r['items'])==0 or r is None):
		print("Nothing found")

	else:
		while(i<len(r['items'])):
			print(r['items'][i]['link'])
			i=i+1