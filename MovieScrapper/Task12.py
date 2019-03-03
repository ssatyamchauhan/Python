import requests
import json
from bs4 import BeautifulSoup
import os.path
from os import path
def scrape_movie_cast(movie_caste_url):
    r=requests.get(movie_caste_url)
    a=r.text
    parse=BeautifulSoup(a,"html.parser")
    cast=parse.find("div",attrs={"id":"fullcredits_content","class":"header"})
    table=cast.find("table",class_="cast_list")
    trs=table.find_all("tr")
    cast_list=[]
    for tr in trs:
        td=tr.find_all("td",class_=None)
        for i in td:
            anchor=i.find("a").text.strip()
            href=i.a["href"]
            count=0
            imdbid=""
            for j in href:
                if j=="/":
                    count+=1
                    if count==3:
                        # print (imdbid),
                        break
                    else:
                        imdbid=""
                else:
                    imdbid=imdbid+j
            cast_dic={
            "imdbid":imdbid,
            "name":anchor
            }
            cast_list.append(cast_dic)


    return cast_list



# user=input("enter the url")
def casting(user):
    e=user.index("e")+2
    id=""
    for i in range(e,len(user)):
        if user[i]=="/":
            break
        else:
            id=id+user[i]
    id=id+"_cast.json"
    url=os.path.join("/home/mrsing/Desktop/Webscraping/cast_files/",id)
    exists=path.exists(url)
    if exists:
        with open(url,"r+") as f:
            var=json.load(f)
            # print (var)
            return var
    else:
        a=scrape_movie_cast(user)
        with open(url,"w") as f:
            b=json.dumps(a)
            var=f.write(b)
        return a
# user=input("enter your url")
# print(casting(user))
