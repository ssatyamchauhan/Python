import requests

from bs4 import BeautifulSoup

All_Details={}
def movie_details(user):
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
	All_Details["name"]=name_of_movie
	# print (var)
	
	article=parse.find("div", attrs={"class":"article","id":"titleDetails"})
	alldiv=article.find_all("div",class_="txt-block")
	for div in alldiv:
		if div.find("h4") in div:
			h4=div.find("h4").text
			if "Country:"==h4:
				anchor=div.find("a")
				Country=anchor.text
				All_Details["country"]=Country
				# print (Country)
			elif "Language:"== h4:
				anchor=div.find_all("a")
				Languages=[k.text for k in anchor]
				All_Details["languages"]=Languages
				# print (Languages)
			elif "Runtime:"==h4:
				Runtime=div.find("time").text
				All_Details["runtime"]=Runtime
		else:
			continue
		

#########-----------------Genre-------------------------#################
	titleStoryLine=parse.find("div",attrs={"class":"article","id":"titleStoryLine"})
	Genrediv=titleStoryLine.find_all("div",class_="see-more inline canwrap")
	for i in Genrediv:
		h4=i.find("h4").text
		if "Genres:"==h4:
			anchor=i.find_all("a")
			genre=[j.text for j in anchor]
			All_Details["genre"]=genre
			# print (genre)

##########-----------------Next Way To find Out Runtime-----------------------################

	# subtext=parse.find("div",class_="subtext")
	# a=subtext.find("time").text
	# Runtime=0
	# j=60
	# for i in range(len(a)):
	# 	if a[i].isdigit():
	# 		if a[i+1].isdigit():
	# 			k=int(a[i])*10
	# 			Runtime=Runtime+k
	# 		else:
	# 			k=int(a[i])*j
	# 			Runtime=Runtime+k
	# 			j=1

##########------------------Director---------------------################
	movie_director=parse.find("div",class_="credit_summary_item")
	director=movie_director.find_all("a")
	directors=[a.text for a in director]
	All_Details["director"]=directors
	# print (directors)

##########------------------Bio-------------------------################
	Bio=parse.find("div",class_="summary_text").text.strip()
	All_Details["bio"]=Bio
	# print (Bio)

##########------------------Poster-link-----------------###############
	poster=parse.find("div",class_="poster")
	poster_anchor=poster.find("a").img['src']
	All_Details["poster_image_url"]=poster_anchor
	# print (poster_anchor)

#########-------------------Dictionary------------------###############
	
	print (All_Details)
user=str(input("enter the url: "))
movie_details(user)

