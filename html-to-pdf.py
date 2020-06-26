
##############################################################
################# HTML to PDF Document Converter #############
##############################################################
# This is a HTML to PDF converter that converts all the
# files inside the htmlResults directory into PDF. The
# results of the conversion is placed inside the pdfResults
# directory. Uses the following dependencies:
# - os - use pip to install
# - pdfkit - use pip to install
# - pdfcrowd - use pip to install
# - wkhtmltopdf - downloaded and added to path

import os
import pdfkit
import pdfcrowd

# Our target directory
inputDir = "./htmlResults"

# Loops through target directory
for filename in os.listdir(inputDir):
    # looks for files that end with .html
    if filename.endswith(".html"):
        # remove the html- from front of file
        strippedFilename0 = filename.replace("html-", "")
        # remove the trailing .html file type
        strippedFilenameFinal = strippedFilename0.replace(".html", "")
        # use pdfkit to output the PDF files to pdfResults dir
        pdfkit.from_file(os.path.join(inputDir, filename),
                         "./pdfResults/pdf-{}.pdf".format(strippedFilenameFinal))
        continue
    else:
        continue
