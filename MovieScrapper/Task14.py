import requests
from Task13 import movie_details_cast
from webscraping1 import scrap_top_list
def analysis_co_actors():
    list_of_5_actors=[]
    task1=scrap_top_list()
    count=0
    for i in task1:
        url=i["url"]
        count+=1
        task14=movie_details_cast(url)
        casts=task14["cast"]
        list1=[]
        k=0
        for j in casts:
            cast=j["imdbid"]
            if k==5:
                list_of_5_actors.append(list1)
                break
            k+=1
            if cast not in list1:
                list1.append(cast)

        if count == 5:
            print (list_of_5_actors)
            break

    for i in list_of_5_actors:



analysis_co_actors()
