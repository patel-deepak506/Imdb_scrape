from pprint import pprint
from bs4 import BeautifulSoup
import requests

url = (" https://www.imdb.com/india/top-rated-indian-movies/")
page=requests.get(url)
soup= BeautifulSoup(page.text,"html.parser")

def scrape_top_list():
	main_div= soup.find('div',class_="lister")
	body=main_div.find('tbody',class_="lister-list")
	res=body.find_all('tr')
	
	movie_rank = []
	movie_name = []
	years_of_realease = []
	movie_ratings = []
	movie_url = []
	rank=0

	for i in res:
		rank=rank+1
		movie_rank.append(rank)	

		title = i.find('td',class_="titleColumn").a.get_text()
		movie_name.append(title)

		year = i.find('td',class_="titleColumn").span.get_text()
		years_of_realease.append(year)

		ratings = i.find('td',class_="ratingColumn imdbRating").strong.get_text()
		movie_ratings.append(ratings)

		watch_list = i.find('td',class_="titleColumn").a ['href']
		url = "https://www.imdb.com" + watch_list
		movie_url.append(url)

	Top_Movie = []
	details = {"rank":" ", "name":" ","year":" ","ratings":" ","url":" " }
	for movie in range(0,250):
		details["rank"] = (movie_rank[movie])
		details["name"] = str(movie_name[movie])
		# years_of_realease[movie] = years_of_realease[movie[1:5]]
		details["year"] = int(years_of_realease[movie][1:5])
		details["ratings"] = float(movie_ratings[movie])
		details["url"] = str(movie_url[movie])
		Top_Movie.append(details.copy())
	return (Top_Movie)

screat=scrape_top_list()

def group_by_year(movies):
	years = []
	for i in movies:
		year = i["year"]
		if year  not in years:
			years.append(year)
	movie_dict = {i:[]for i in years}
	for i in movies:
		year = (i["year"])
		for j in movie_dict:
			if int(j) == int(year):
				movie_dict[j].append(i)
	return movie_dict

# pprint(group_by_year(screat))ar(screat))


decade=group_by_year(screat)

def group_by_decade(movies):
	list1  = []
	for i in movies:
		# print(len(i))
		dec= i%10
		sub=i-dec
		if sub not in list1:
			list1.append(sub)
		# print(list1)
	movie_dec = {}
	list1.sort()
	# print(list1)
	for j in list1:
		movie_dec[j] = []
		for j in movie_dec:
			dec10 = j+9
			# print(dec10)
			for m in movies:
				if m  <= dec10 and m>=j:
					for k in movies[m]:
						movie_dec[j].append(k)
	return(movie_dec)			


		# else:
		# 	print("false")



pprint(group_by_decade(decade))


