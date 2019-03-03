import os.path
from os import path
import json
from Task5 import get_movie_list_details
from Task5 import scrap_top_list
a=scrap_top_list()
movie_list=a[:250]

exists=path.exists("/home/satya/Desktop/Webscraping/task11.json")

if exists:
	with open("task11.json") as f:
		var=json.load(f)
		print (var)
else:
	def analyse_language_and_directors(movie_list):
		task10=get_movie_list_details(movie_list)
		list_of_genres=[]
		for i in task10:
			genre=i["Genre"]
			for j in genre:
				if j not in list_of_genres:
					list_of_genres.append(j)
		
		dic={}
		for i in list_of_genres:
			count=0
			for j in task10:
				genre=j["Genre"]
				if i in genre:
					count+=1
			dic[i]=count
		with open("task11.json","w") as f :
			a=json.dumps(dic)
			f.write(a)

	analyse_language_and_directors(movie_list)