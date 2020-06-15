# Author: Joseph Bernadas
# Description: Converts old style tables to Bootstrap ready
# Version: 1.0.0
# License: GPL version 3
# Date: 2020/06/14

from bs4 import BeautifulSoup
import lxml
import requests
import re
import os

##########################################
##### Link Crawler/Harvester begins ######
##########################################

# The URL where we plan to get our links from
targetUrl = "https://trip.llnl.gov/results.html"

# Initialize empty array to hold all the harvested links
harvestedLinks = []

# Gets the text version targetURL DOM and stores in variable
html_page = requests.get(targetUrl).text
# Use BeautifulSoup to store all data from page
initialSoup = BeautifulSoup(html_page, "lxml")
# From the above data we looks for those tables which contain the final info we need
harvestTable = initialSoup.find_all('table', attrs={'width': '714'})

# Loops through all the valid tables and harvest links and store it into harvestedLinks array
for link in initialSoup.find_all('a', attrs={'href': re.compile('^results')}):
    harvestedLinks.append(link.get('href'))

###########################################
##### / End of Link Crawler/Harvester #####
###########################################

###########################################
######### Table Re begins ###########
###########################################

# Stores incremented value
i = 0

# Loops through each of the harvested links
for harvestedLink in harvestedLinks:
    # Used for the HTML header and body (Comment-out to output just the tables without HTML 5 header)
    htmlHead = """<!DOCTYPE html><html lang="en"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Document</title> <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous"> <style>body{text-align: center}.link-wrapper{width: 100%; text-align: center}a.btn.btn-default{padding: 3px 20px; margin: 5px}.navbar-nav{float:none; margin: 0 auto; display: table; table-layout: fixed;}</style> </head> <body> <div class='container'><div class='row'><div class='col-12'>"""
    # Closes the above HTML and body (Comment-out to output plain tables)
    htmlEnd = """</div></div></div></body></html>"""
    # The navigation bar
    anchorLinksNav = """<div class='link-wrapper'><ul class="nav navbar-nav"> <li><a class='btn btn-default' href='#i125'>I-125</a></li><li><a class='btn btn-default' href='#i131'>I-131</a></li></ul></div>"""
    # The invisible anchor tags for scrolling to sections of page
    anchorI125 = "<a id='i125'></a><p><h3>I-125 Results</h3></p>"
    anchorI131 = "<a id='i131'></a><p><h3>I-131 Results</h3></p>"

    # Stitches together base URL and the harvestedLink
    fullUrl = requests.get("https://trip.llnl.gov/" + harvestedLink).text

    # Parses the HTML content
    soup = BeautifulSoup(fullUrl, 'lxml')
    # Stores the page's title
    pageTitle = soup.h2
    # Stores the page's sub-title
    pageSubTitle = soup.h4

    # Finds only the tables with a border attribute of 4
    tables = soup.find_all('table', attrs={"border": "4"})

    # Used for tables only with anchor tags and nav-links
    tables.insert(0, anchorLinksNav)
    tables.insert(1, anchorI125)
    tables.insert(5, anchorI131)

    # Used for displaying as HTML webpage (Comment-out to output just the tables)
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
    for tag in soup.find_all('td', attrs={'bgcolor': '#999999'}):
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

##### / End of table maker. #####
