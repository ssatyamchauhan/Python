import requests

from bs4 import BeautifulSoup 	

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
	main_link="http//:www.imdb.com"+link
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
# print(Dictionary_list)
# print (movie_rank)
# print (movie_name)
# print (movie_year)
# print (movie_rating)
# print (movie_link)
####################--------Task3-----------------#################
Task3_dic={}
j='(1971)'
for i in movie_year:  # to find out the minimum year of movies and maximm year of movies.
	if int(i[1:-1])>int(j[1:-1]):
		j=i
# print (j)

for i in (range(1950,2020,10)):
	list_task3=[]
	for j in range(i,i+10):
		for k in Dictionary_list:
			if int(k["year"][1:-1])==j:
				dic={
					"name": k["name"],
					"year": k["year"],
					# "position": k["position"],
					"rating": k["rating"]
					# "url": k["url"]
					}
				list_task3.append(dic)

	Task3_dic[i]=list_task3
print (Task3_dic)




