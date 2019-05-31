<h1 align="center" > IMDB movie Scrapper </h1>

In this project, I have made a IMDB Scraper (https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in) in which I have scraped a total of 250 movies using BeautifulSoup and Requests Library, and performed different analysis based on years, decades, genres, directors, languages and casts. 
I have also stored all the data in the cache files in json format.

## Requirements

### BeautifulSoup

Beautiful Soup is a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping. If you're using Linux based OS, you can install BeautifulSoup using following command in terminal.

Here, pip is a package-management system used to install and manage software packages written in Python.

```
sudo apt-get update && sudo apt-get install python3-pip
pip3 install beautifulsoup4
```

### Requests Library

Requests is an Apache2 Licensed HTTP library, written in Python. Requests will allow you to send HTTP/1.1 requests using Python.
You can install requests library using following code in your terminal in Linux.

`pip3 install requests`

After finishing installation process above, you can run the tasks, using `python3 file_name.py`.


<h1 align="center">Explained all Tasks</h1>

<h3> 12+ tasks, In each task performed different analysis like cast, genre, language, decades and their ratings </h3> 

<h3>Task1: In this task, Scraped top250-indian-rated-movies in which movie-name, rating, position and url are inclued of each movie</h3>
<h3>Task2: Performed group by year analysis in which for every year there movies are grouped in a list</h3>
<h3>Task3: Analysing the movies using decade group by year so that easly can find movies of 10 years in a list</h3>
<h3>Task4: Scraped movie-name, poster-image-url, bio, runtime, country and genre of each name.</h3>
<h3>Task5: Performed the same action of task4 on 250 movie top-rated-indian-movies.</h3>
<h3>Task6: Count all the movies to check-out how many movies are in each language.</h3>
<h3>Task7: Count for directors to check-out each directore worked in how many movies.</h3>
<h3>Task8: performed cache action to store the data in local storage so that our programmer can be fast.</h3>
<h3>Task9: Using time module of python to sleep for 3sec after each movie scrap.</h3>
<h3>Task10: Performed an interesting analysis in which we are counting of each language movies worked each director.</h3>
<h3>Task11: Analysed the movie on the basis of each genre like drama, comedy and horror etc.</h3>
<h3>Task12: Scraped the cast of each movie and of each also scraped thier imdbId.</h3>
<h3>Task13: Listed all the casts of each movie in a dictionary, named key cast.</h3>
