from pprint import pprint
from bs4 import BeautifulSoup
import requests
import json

url = (" https://www.imdb.com/india/top-rated-indian-movies/")
page=requests.get(url)
soup= BeautifulSoup(page.text,"html.parser")

def scrape_top_list():
	main_div= soup.find('div',class_="lister")
	body=main_div.find('tbody',class_="lister-list")
	res=body.find_all('tr')
	Top_Movie = []
	movie_rank = []
	movie_name = []
	years_of_realease = []
	movie_ratings = []
	movie_url = []
	rank=0

	for i in res:
		rank=rank+1
		# movie_rank.append(rank)	

		title = i.find('td',class_="titleColumn").a.get_text()
		# movie_name.append(title)

		year = i.find('td',class_="titleColumn").span.get_text()
		# years_of_realease.append(year)

		ratings = i.find('td',class_="ratingColumn imdbRating").strong.get_text()
		# movie_ratings.append(ratings)

		watch_list = i.find('td',class_="titleColumn").a ['href']
		url = "https://www.imdb.com" + watch_list
		# movie_url.append(url)

	# Top_Movie = []
		details = {"rank":" ", "name":" ","year":" ","ratings":" ","url":" " }
		details["rank"] = rank
		details["name"] = title


		details["year"] = (year[1:5])
		details["ratings"] = float(ratings)
		details["url"] = str(url)
		Top_Movie.append(details)
		# pprint(Top_Movie)

	return (Top_Movie)
if __name__=="__main__":
	pprint(scrape_top_list())









 

