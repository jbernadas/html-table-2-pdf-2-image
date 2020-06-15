============
TABLE CONVERTER
============

Crawls and harvest links then, recursively looks for tables to reconstitute from old style tables to Bootstrap ready tables.

Features:

- Crawls the target URL to find targettable links.
- Harvest the table links and stores them in an array.
- Strips away the table's unnecessary attributes to recreate it as a Bootstrap ready version. 

Contributions and comments are welcome using Github at: 
http://github.com/jbernadas/table-converter

Please note that Table-Converter requires:

- BeautifulSoup 4
- Requests
- Re
- Os
- Lxml

Installation
============

:: 
  git clone https://github.com/jbernadas/table-converter
:: 
  cd into the directory created

Create the results directory:
::
  mkdir results
  
Use pip to install all the above requirements.

Configuration
=============

None.

Documentation
=============

You can tweak the arguments and parameters to make it find the necessary table targets.

Usage
=====

cd into the root directory.
python3 table-converter.py

You will find the result inside the results folder.

Bugs & Contribution
===================

Please use Github to report bugs, feature requests and submit your code:
http://github.com/jbernadas/table-converter

:author: Joseph Bernadas
:date: 2020/06/14
