import json,requests
from pprint import pprint
from bs4 import BeautifulSoup
from task12 import scrape_movie_cast


def movie_cast_details():
	data=scrape_movie_cast
	json_file=open("all_movies_details.json","r")
	data=json.load(json_file)
	# pprint(data)
	for i in range(len(data)):
		a=(data[i])
		# print(a)
		b=[]
		for j in a:
			c=[]
			b.append(j)
		# pprint(b)
	dct={}
	for key in b:
		value=(a[key])
		# pprint(value)
		dct[key]=value
		dct["cast"]=data
	pprint(dct)



movie_cast_details()	
