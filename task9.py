import random 
import json
import time 
from task1 import scrape_top_list
from task4 import scrape_movie_details

main_list=[]
def json_data():
	a=scrape_top_list()
	for i in a:
		b=i["url"]
		# print(b)
		time1=random.randint(1,4)
		time.sleep(time1)
		c=scrape_movie_details(b)
		main_list.append(c)

		link=(i["url"][27:36])
		d=link+".json"
		with open(d,"w+")as json_file:
			json.dump(c,json_file)
		with open("all_movies_details.json",'w+')as json_data:
			json.dump(main_list,json_data)
		print("success")  

		

json_data()