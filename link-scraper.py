from bs4 import BeautifulSoup
import lxml
import requests
import re

baseUrl = "https://trip.llnl.gov/"

targetUrl = "https://trip.llnl.gov/results.html"

harvestedLinks = []

html_page = requests.get(targetUrl).text
soup = BeautifulSoup(html_page, "lxml")
tables = soup.find_all('table', attrs={'width': '714'})

for link in soup.find_all('a', attrs={'href': re.compile('^results')}):
    harvestedLinks.append(link.get('href'))

# # Open the file named table.html, if it does not exist create it
# with open("links.py", "w+", encoding='utf-8') as url:
#     for link in harvestedLinks:
#         url.write(str(link))
