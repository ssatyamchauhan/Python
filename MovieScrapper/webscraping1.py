import requests

from bs4 import BeautifulSoup 	
def scrap_top_list():
	r=requests.get("https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in")

	page=r.text
	parse=BeautifulSoup(page,"html.parser")
	# heading=parse.find("h1").text
	# print (heading)
	# title=parse.find("title").text
	# print(title)
	lister=parse.find("div",class_="lister")
	tbody=lister.find("tbody",class_="lister-list")
	j=1
	movie_rank=[]
	movie_name=[]
	movie_year=[]
	movie_rating=[]
	movie_link=[]
	Dictionary_list=[]
	trs=tbody.find_all("tr")
	for tr in trs:
		td=tr.find("td", class_="titleColumn")
		movie_rank.append(j)
		name=td.find("a").text
		movie_name.append(name)
		year=td.find("span").text
		movie_year.append(year)
		rating=tr.find("td",class_="ratingColumn imdbRating").text.strip()
		movie_rating.append(rating)
		link=tr.find("td", class_="titleColumn").a["href"]
		main_link="http://www.imdb.com"+link
		movie_link.append(main_link)
		j+=1
		# print (a),
		# print (j)
		
		# print (td)
		# print (td)
		# print (td)
		# print ("....................................................................")
		# for i in td:
		# 	if '.' not in i:
					
			# else:
			# 	j+=1
			# 	break
	for i in range(250):
		dic={
	    "name": movie_name[i],
	    "year": movie_year[i],
	    "position": movie_rank[i],
	    "rating": movie_rating[i],
	    "url": movie_link[i]
	  }
		Dictionary_list.append(dic)
	return Dictionary_list
	# print(Dictionary_list)
	# print (movie_rank)
	# print (movie_name)
	# print (movie_year)
	# print (movie_rating)
	# print (movie_link)

################----------------------Task2------------------##################################

	# Task2={}
	# for j in movie_year:
	# 	list_task2=[]
	# 	for k in range(250):
	# 		if j==Dictionary_list[k]["year"]:
	# 			dic2={"name":Dictionary_list[k]["name"],"year":j,"position":Dictionary_list[k]["position"],"rating":Dictionary_list[k]["rating"],"url":Dictionary_list[k]["url"]}
	# 			list_task2.append(dic2)
	# 	Task2[j] = list_task2
	# print (Task2)
scrap_top_list()

