import json
from pprint import pprint


def analyse_language_and_directors():
	file = open("all_movies_details.json","r")
	data=json.load(file)
	# pprint(data)
	# for i in data:
	# 	a=i["Director"]
	# pprint(a)
	
	director_dic={}
	for i in data:
		language_dic={}
		for j in data:
			count=0
			for k in data:
				if j['language']==k['language'] and i['Director']==j['Director']==k['Director'] and j['language'] not in language_dic:
					count+=1
			if count!=0:
				language_dic[j['language']]=count
		director_dic[i['Director']]=language_dic
	pprint(director_dic)


analyse_language_and_directors()