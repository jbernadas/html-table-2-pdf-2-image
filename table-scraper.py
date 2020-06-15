from bs4 import BeautifulSoup
import lxml
import requests
import re
import os

######### Links Harvester begins ########

targetUrl = "https://trip.llnl.gov/results.html"

harvestedLinks = ["results/results2019-2.html"]

# html_page = requests.get(targetUrl).text
# soup = BeautifulSoup(html_page, "lxml")
# harvestTable = soup.find_all('table', attrs={'width': '714'})

# for link in soup.find_all('a', attrs={'href': re.compile('^results')}):
#     harvestedLinks.append(link.get('href'))

i = 0

######## Table Maker begins #######
for harvestedLink in harvestedLinks:

    htmlHead = """<!DOCTYPE html><html lang="en"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Document</title> <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous"> <style>body{text-align: center}.link-wrapper{width: 100%; text-align: center}a.btn.btn-default{padding: 3px 20px; margin: 5px}.navbar-nav{float:none; margin: 0 auto; display: table; table-layout: fixed;}</style> </head> <body> <div class='container'><div class='row'><div class='col-12'>"""

    htmlEnd = """</div></div></div></body></html>"""

    anchorLinksNav = """<div class='link-wrapper'><ul class="nav navbar-nav"> <li><a class='btn btn-default' href='#i125'>I-125</a></li><li><a class='btn btn-default' href='#i131'>I-131</a></li></ul></div>"""

    anchorI125 = "<a id='i125'></a><p><h3>I-125 Results</h3></p>"
    anchorI131 = "<a id='i131'></a><p><h3>I-131 Results</h3></p>"

    html_content = requests.get("https://trip.llnl.gov/" + harvestedLink).text

    # Parses the HTML content
    soup = BeautifulSoup(html_content, 'lxml')
    pageTitle = soup.h2
    pageSubTitle = soup.h4

    tables = soup.find_all('table', attrs={"border": "4"})

    # Tables only with anchor tags and links
    tables.insert(0, anchorLinksNav)
    tables.insert(1, anchorI125)
    tables.insert(5, anchorI131)

    # Used for displaying as HTML webpage
    tables.insert(0, htmlHead)
    tables.append(htmlEnd)
    tables.insert(1, pageTitle)
    tables.insert(2, pageSubTitle)

    # Preliminary attributes to remove
    REMOVE_ATTRIBUTES = [
        'cellpadding', 'cellspacing', 'width', 'align', 'class', 'style'
    ]

    # Recursively remove above listed attributes
    for attribute in REMOVE_ATTRIBUTES:
        for tag in soup.find_all(attrs={attribute: True}):
            del tag[attribute]

    # Finds and removes all valign=top attributes AND child elements
    for tag in soup.find_all(attrs={'valign': 'top'}):
        tag.decompose()

    # Finds and removes rest of valign attributes
    for tag in soup.find_all(attrs={'valign': 'bottom'}):
        del tag['valign']

    # Finds and removes border attributes, then adds class to table elements
    for tag in soup.find_all('table', attrs={'border': '4'}):
        del tag['border']
        tag['class'] = 'table table-striped table-bordered'

    # Finds all br tags and removes them
    for tag in soup.find_all('br'):
        tag.decompose()

    # Open the file named table.html, if it does not exist create it
    with open("./results/index%s.html" % (i), "w+", encoding='utf-8') as file:
        for table in tables:
            file.write(str(table))
    i += 1
