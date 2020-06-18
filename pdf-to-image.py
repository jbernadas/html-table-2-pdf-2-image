# This is a PDF to Image converter script.
# It uses as dependencies:
# - PDF2Image
# - Poppler
# - os


import os
from pdf2image import convert_from_path, convert_from_bytes

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

# Target directory for taking PDF files to convert
inputDir = './pdfResults'

# Increment variable (must use 1000 or else not sorting properly)
i = 1000

# Loop through target directory
for filename in os.listdir(inputDir):
    # we only want PDF files
    if filename.endswith(".pdf"):
        # use PDF2Image
        image = convert_from_path(
            # Rest of this are parameters of PDF2Image output file
            # Input string
            os.path.join(inputDir, filename),
            # Can be png too
            fmt='jpeg',
            # Output folder
            output_folder="./imgResults",
            # Resolution quality of image can use 200 or 600
            dpi=300,
            # Takes image of first page
            first_page=1,
            # We only want first page no following page of
            # this PDF document
            last_page=1,
            # Output file name
            output_file='table%s' % (i),
            # Single_file mode should be true,
            # because iteration already taken care of
            # by for-loop, or else won't work on multiple files
            single_file=True,
            # Width of output image
            size=100)
        i += 1
        continue
    else:
        continue
