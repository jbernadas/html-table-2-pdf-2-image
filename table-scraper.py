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

# Preliminary attributes to remove
REMOVE_ATTRIBUTES = [
  'cellpadding', 'cellspacing', 'width', 'align', 'class', 'style'
] 

# Recursively remove above listed attributes
for attribute in REMOVE_ATTRIBUTES:
  for tag in soup.find_all(attrs={attribute: True}):
    del tag[attribute]

# Removes all valign=top attributes AND child elements
for tag in soup.find_all(attrs={'valign': 'top'}):
  tag.decompose()

# Removes rest of valign attributes
for tag in soup.find_all(attrs={'valign': 'bottom'}):
  del tag['valign']

# Removes border attributes, then adds class to table elements
for tag in soup.find_all('table', attrs={'border': '4'}):
  del tag['border']
  tag['class']='table table-striped table-bordered'

for tag in soup.find_all('br'):
  tag.decompose()

print(pageTitle)
print(pageSubTitle)
print("<h3>I-125 Results</h3>")
print("<!-------Table 1------->")
print(tables[0])
print('<p>&nbsp;</p>')
print("<!------Table 2-------->")
print(tables[1])
print('<p>&nbsp;</p>')
print("<!-------Table 3-------->")
print(tables[2])
print('<p>&nbsp;</p>')
print("<h3>I-131 Results</h3>")
print("<!-------Table 4-------->")
print(tables[3])
print('<p>&nbsp;</p>')
print("<!-------Table 5-------->")
print(tables[4])
print('<p>&nbsp;</p>')
print("<!-------Table 6-------->")
print(tables[5])
