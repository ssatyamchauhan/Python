from Task5 import get_movie_list_details
from webscraping1 import scrap_top_list
task1=scrap_top_list()
top_ten_movie=task1[0:10]


def analyse_movies_language(top_ten_movie):
	task5=get_movie_list_details(top_ten_movie)
	hindi=0
	malayalam=0
	english=0
	telgu=0
	tamil=0
	for j in task5:
		k=j["Languages"]
		for i in k:
			if i=="Hindi":
				hindi+=1
			if i=="English":
				english+=1
			if i=="Malayalam":
				malayalam+=1
			if i=="Telugu":
				telgu+=1
			if i=="Tamil":
				tamil+=1
	dic={"Hindi":hindi,"English":english,"Malayalam":malayalam,"Telugu":telgu,"Tamil":tamil}
	return dic

print (analyse_movies_language(top_ten_movie))