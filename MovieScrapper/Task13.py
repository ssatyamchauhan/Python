from Task12 import casting
import pprint
from Task5 import scrap_movie_details
def movie_details_cast(user):
    task5=scrap_movie_details(user)
    task12=casting(user)
    dic=task5
    dic["cast"]=task12
    return dic
    # pprint.pprint(dic)

# user=input("enter  the  url")
# movie_details_cast(user)
