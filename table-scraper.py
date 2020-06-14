from bs4 import BeautifulSoup
import requests
# import os

url =  "https://trip.llnl.gov/results/results2018-1.html"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text
  
# Parses the HTML content
soup = BeautifulSoup(html_content, "lxml")
pageTitle = soup.h2
pageSubTitle = soup.h4
tables = soup.find_all('table', attrs={"border": "4"})

print(pageTitle)
print(pageSubTitle)
print(tables)

with open("")
