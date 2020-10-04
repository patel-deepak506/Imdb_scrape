import os,json,requests
from task1 import scrape_top_list
from pprint import pprint
from bs4 import BeautifulSoup


movie_details_list=[]
def scrape_movie(url):
	for i in url:
		link=i["url"]
		page = requests.get(link)
		soup = BeautifulSoup(page.text,"html.parser")
		main_div = soup.find("div",class_="title_wrapper").h1.text
		movie_name = ""
		for i in main_div:
			if "(" not in i:
				movie_name = (movie_name+i).strip()
			else:
				break
		next_div = soup.find("div",class_="subtext").time.text.strip()
		time_hour = int(next_div[0])*60
		if "min" in next_div:
			minutes = int(next_div[3:].strip("min"))
			movie_time = time_hour + minutes
		else:
			movie_time = time_hour

		genre = soup.find("div",class_="subtext").a.text

		summary = soup.find("div",class_="plot_summary")
		movie_bio = summary.find("div",class_="summary_text").text.strip()

		Director = summary.find("div",class_="credit_summary_item").a.text.strip()
		
		poster_image_url=soup.find("div",class_="poster").a["href"]
		poster_image = "https://www.imdb.com" + poster_image_url

		sub_div = soup.find("div",class_="article",id="titleDetails")
		details =sub_div.find_all("div",class_="txt-block")
		a=[]
		for i in details:
			if "Language"in i.text:
				language=i.find("a").text


			if "Country" in i.text:
				country = i.find("a").text

		movie_details_dict = {"name": "","Director":" ","bio":"","runtime":"","gener":"","poster_image_url":"","country":" ","language":""}	
		# movie_details_dict={}
		movie_details_dict["name"] = movie_name
		movie_details_dict["Director"] = Director
		movie_details_dict["bio"] = movie_bio
		movie_details_dict["runtime"] = movie_time
		movie_details_dict["gener"] = genre
		movie_details_dict["poster_image_url"] = poster_image
		movie_details_dict["country"] = country
		movie_details_dict["language"] = language
		movie_details_list.append(movie_details_dict)

	return (movie_details_list)

movie_list=scrape_top_list()
if __name__ == "__main__":
	pprint(scrape_movie(movie_list[0:10]))