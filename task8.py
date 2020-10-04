import json,requests
from pprint import pprint 
from bs4 import BeautifulSoup
from task4 import scrape_movie_details
from task1 import scrape_top_list

data =scrape_top_list()
print(data)

def movies_json():

	n=scrape_top_list()
	for i in n:
		o=i["url"]
		# print(o)
		l=scrape_movie_details(o)

		movies_link=(i["url"][27:36])
		m=movies_link+".json"
		with open(m,"w+")as json_file:
			json.dump(l,json_file)
		print("succss")  
	
movies_json()