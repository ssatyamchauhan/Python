import os.path
from os import path
import json
from Task5 import get_movie_list_details
from Task5 import scrap_top_list
a=scrap_top_list()
movie_list=a[:250]

exists=path.exists("/home/satya/Desktop/Webscraping/task10.json")

if exists:
	with open("task10.json") as f:
		var=json.load(f)
		print (var)
else:
	def analyse_language_and_directors(movie_list):
		task10=get_movie_list_details(movie_list)
		list_of_directors=[]
		list_of_languages=[]
		for i in task10:
			director=i["directors"]
			for j in director:
				if j not in list_of_directors:
					list_of_directors.append(j)

		for i in task10:
			language=i["Languages"]
			for j in language:
				if j not in list_of_languages:
					list_of_languages.append(j)

		main_dic={}
		for i in list_of_directors:
			dic={}
			for j in list_of_languages:
				count=0
				for k in task10:
					direct=k["directors"]
					lan=k["Languages"]
					if i in direct:
						if j in lan:
							count+=1
				if count>0:
					dic[j]=count
			main_dic[i]=dic
		with open("task10.json","w") as f:
			var=json.dumps(main_dic)
			f.write(var)

	analyse_language_and_directors(movie_list)