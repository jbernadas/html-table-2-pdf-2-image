from bs4 import BeautifulSoup
import lxml
import requests
# import os

url =  "https://trip.llnl.gov/results/results2018-1.html"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text
  
# Parses the HTML content
soup = BeautifulSoup(html_content, 'lxml')
pageTitle = soup.h2
pageSubTitle = soup.h4
tables = soup.find_all('table', attrs={"border": "4"})

# print(pageTitle)
# print(pageSubTitle)
print("<!-------Table 1------->")
print(tables[0])
print("<!------Table 2-------->")
print(tables[1])
print("<!-------Table 3-------->")
print(tables[2])
print("<!-------Table 4-------->")
print(tables[3])
print("<!-------Table 5-------->")
print(tables[4])
print("<!-------Table 6-------->")
print(tables[5])
