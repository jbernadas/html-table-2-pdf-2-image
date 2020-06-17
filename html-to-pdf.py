# This is a HTML to PDF converter that converts all the files inside htmlResults directory into PDF.
# The results of the conversion is placed inside the pdfResults directory.
# Uses the following dependencies: os, pdfkit, pdfcrowd, wkhtmltopdf
# (the first 3 installed with pip, last one, wkhtmltopdf, is downloaded and added to path environment)

import os
import pdfkit
import pdfcrowd

directory = "./htmlResults"

i = 0

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        pdfkit.from_file(os.path.join(directory, filename),
                         "./pdfResults/table{}.pdf".format(i))
        i += 1
        # print(os.path.join(directory, filename))
        continue
    else:
        continue
