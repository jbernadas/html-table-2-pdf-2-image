============
HTML-TABLE-2-PDF-2-IMAGE
============

This is a HTML-table to PDF to image converter. It first crawls and harvests links, then recursively looks for tables and cleans it of extra attributes then builds new Bootstrap ready tables. Also has a separate script for converting HTML tables to PDF and another separate script for converting PDFs to images, i.e., JPG or PNG.

Features:

- Crawls the target URL to find targettable links.
- Harvest the table links and stores them in an array.
- Strips away the table's unnecessary attributes to recreate it as a Bootstrap ready version. 

Contributions and comments are welcome at: 
http://github.com/jbernadas/table-converter

These are the dependencies it requires:

- BeautifulSoup 4
- Requests
- Re
- Os
- Lxml

Installation
============

Clone as usual:
:: 
  git clone https://github.com/jbernadas/table-converter

Go inside the created directory: 
:: 
  cd table-converter

Use pip to install all the above requirements:
::
  pip install bs4
  pip install Requests
  pip install Re
  pip install Lxml

Configuration
=============

None.

Documentation
=============

You can tweak the arguments and parameters to make it find the necessary table targets.

Usage
=====

cd into the root directory:
::
  cd table-converter

Fire it up, it takes a few seconds to convert a hundred tables:
::
  python3 table-converter.py

You will find the result inside the htmlResults folder.

If you wish to further convert the HTML output into PDF files, run the html-to-pdf.py:
::
  python3 html-to-pdf.py

You will find the result inside the pdfResults folder.

Bugs & Contribution
===================

Please use Github to report bugs, feature requests and submit your code:
http://github.com/jbernadas/table-converter

:author: Joseph Bernadas
:version: 1.0.0
:date: 2020/06/14
:license: GPL version 3
