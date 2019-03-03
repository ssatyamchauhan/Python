import requests
from webscraping1 import scrap_top_list
task1 = scrap_top_list()
# print (task1[1:5])
from bs4 import BeautifulSoup
list_of_10_movies=[]
def scrap_movie_details(user):
	All_Details={}
	r=requests.get(user)
	a=r.text
	parse=BeautifulSoup(a,"html.parser")
	movie_name=parse.find("h1").text
	name_of_movie=""
	for i in movie_name:
		if i==" ":
			break
		else:
			name_of_movie+=i
	All_Details['Name']=name_of_movie
	# print (var)
	
	article=parse.find("div", attrs={"class":"article","id":"titleDetails"})
	alldiv=article.find_all("div",class_="txt-block")
	for div in alldiv:
		if div.find("h4") in div:
			h4=div.find("h4").text
			if "Country:"==h4:
				anchor=div.find("a")
				Country=anchor.text
				All_Details['Country']=Country
				# print (Country)
			elif "Language:"== h4:
				anchor=div.find_all("a")
				Languages=[k.text for k in anchor]
				All_Details['Languages']=Languages
				# print (Languages)
			elif "Runtime:"==h4:
				time=div.find("time")
				Runtime=time.text
				All_Details['Runtime']=Runtime
				# print (Runtime)

		# else:
		# 	continue
		

#########-----------------Genre-------------------------#################
	titleStoryLine=parse.find("div",attrs={"class":"article","id":"titleStoryLine"})
	Genrediv=titleStoryLine.find_all("div",class_="see-more inline canwrap")
	for i in Genrediv:
		h4=i.find("h4").text
		if "Genres:"==h4:
			anchor=i.find_all("a")
			genre=[j.text for j in anchor]
			All_Details['Genre']=genre
			# print (genre)
			
##########------------------Director---------------------################
	movie_director=parse.find("div",class_="credit_summary_item")
	director=movie_director.find_all("a")
	directors=[a.text for a in director]
	All_Details['directors']=directors
	# print (directors)

##########------------------Bio-------------------------################
	Bio=parse.find("div",class_="summary_text").text.strip()
	All_Details['bio']=Bio
	# print (Bio)

##########------------------Poster-link-----------------###############
	poster=parse.find("div",class_="poster")
	poster_anchor=poster.find("a").img['src']
	All_Details['poster_image_url']=poster_anchor
	# print (poster_anchor)

#########-------------------Dictionary------------------###############

	list_of_10_movies.append(All_Details)

def get_movie_list_details(moviedetails):
	for i in moviedetails:
		url = i['url']
		scrap_movie_details(url)
	return list_of_10_movies
top_ten_movie = task1[:0]
get_movie_list_details(top_ten_movie)
# print (list_of_10_movies)
# # #########-------------Urls-----------------------########################

# user = "https://www.imdb.com/title/tt5074352/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=690bec67-3bd7-45a1-9ab4-4f274a72e602&pf_rd_r=FNZH1QHB6YE046GV2G5X&pf_rd_s=center-4&pf_rd_t=60601&pf_rd_i=india.top-rated-indian-movies&ref_=fea_india_ss_toprated_tt_11"
# print(Movie_details_list(user))