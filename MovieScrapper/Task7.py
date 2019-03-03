from Task5 import get_movie_list_details
from webscraping1 import scrap_top_list
task1=scrap_top_list()
top_ten_movie=task1[0:10]


list_of_directors=[]

dic={}

def analyse_movies_directors(top_ten_movie):
	task5=get_movie_list_details(top_ten_movie)
	for i in task5:
		director=i["directors"]
		for j in director:
			if j in list_of_directors:
				continue
			else:
				list_of_directors.append(j)

	for i in list_of_directors:
		count=0
		for j in task5:
			director=j["directors"]
			if i in director:
				count+=1
		
		dic[i]=count
	return dic



print(analyse_movies_directors(top_ten_movie))