import json,requests
from pprint import pprint
from bs4 import BeautifulSoup
from task1 import scrape_top_list

url=scrape_top_list()

def scrape_movie_cast():
	for i in url:
		link=(i["url"])
		link_list=(link+"fullcredits?ref_=tt_cl_sm#cast")
		page=requests.get(link_list)
		soup= BeautifulSoup(page.text,"html.parser")
		main_div=soup.find("div",class_="article listo")
		table=main_div.find("table",class_="cast_list")
		table_data=table.find_all("td",class_="")

		main_list=[]
		for data in table_data:
			cast_name=(data.text.strip())
			link_name=(data.find("a").get("href"))
			imdb_id=(link_name[6:15])
			dct={"imdb_id":"","name":""}
			dct["imdb_id"]=imdb_id
			dct["name"]=cast_name
			main_list.append(dct)
			dum = json.dumps(main_list)
			# print(main_list)

		with open("main_list.json","w+") as json_data:
			json_data.write(dum)
			print("success")
	json_data.close()
	# return main_list

scrape_movie_cast()
