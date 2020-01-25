import os.path 
from os import path
import requests
import json
exists=path.exists("/home/satya/Desktop/RequestAPI/files.json")
if exists:
	with open("files.json") as f:
		var=json.load(f)
else:
	r=requests.get("http://saral.navgurukul.org/api/courses")
	a=r.text
	with open("files.json","w+") as f:
		var=json.loads(a)
		f.write(json.dumps(var, sort_keys=True, indent=4))
		var=json.loads(a)


def list_of_courses():
	j=0
	for i in var["availableCourses"]:
		print j,
		# print i["name"]
		j+=1
	list_of_Exercises()
def list_of_Exercises():
	j=0
	user=input("enter your input")
	print "      "
	for i in var["availableCourses"]:
		if user==j:
			j=0
			print "Loading......"
			print i["id"],
			print i["name"]
			print "         "
			r=requests.get("http://saral.navgurukul.org/api/courses/"+str(i["id"])+"/exercises")
			a=r.text
			d=json.loads(a)
			e=d["data"]
			for s in e:
				print "\n"+"      ",j,"   "+s["name"]
				j=j+1
			n=input("\nSelect any courses by entering index value: ")
			if n<j:
				while n>=0:
					if n>=0:
						f=e[n]
						if n>=0:
							r=requests.get("http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug="+f["slug"])
							a=r.text
							k=json.loads(a)
							print "\n",k
						s=raw_input("Enter your input: ")
						if s=="p":
							n=n-1
							if n<0:
								print "list indices is out of range\n"
								list_of_courses()
						elif s=="n":
							n+=1
							if n>j-1:
								print "list of indices is out of range\n"
								list_of_courses()
						elif s=="up":
							list_of_courses()
						elif s=="exit":
							print "You are outside of the program"
							break
			else:
				print "index is out of Range\n"
				list_of_courses()

		j=j+1
list_of_courses()
