import os
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter
from wand.image import Image

def generate_thumb(path):
    """

    """

    try:
        FileNotFoundError
    except NameError:
        FileNotFoundError = IOError

    # Open PDF & Extract 1st Page
    pdf_output = PdfFileWriter()

    try:
        pdf_output.addPage(PdfFileReader(file(path, 'rb')).getPage(0))
    except FileNotFoundError:
        print "\nFILE \"{one}\" NOT FOUND ...".format(one=path)
        return False
    except:
        print "\nERROR READING \"{one}\" BY \"PdfFileReader\" ...".format(one=path)
        return False

    pdf_output_file = "{one}_{two}.pdf".format(one=os.path.splitext(path)[0],
                                               two="1stPage")
    outputStream = file(pdf_output_file, "wb")

    # Write 1st Page 2 PDF File
    try:
        pdf_output.write(outputStream)
        outputStream.close()
    except IOError:
        print "\nERROR CREATING FIRST PAGE FILE \"{one}\" ...".format(one=pdf_output_file)
        return False

    # First Page PDF 2 JPG
    jpg_output_file = "{one}.jpg".format(one=os.path.splitext(path)[0])

    try:
        with Image(filename=pdf_output_file) as img:
            img.resize(283, 400)
            img.save(filename=jpg_output_file)
            os.remove(pdf_output_file)
    except:
        print "\nERROR CREATING JPG FILE \"{one}\" ...".format(one=jpg_output_file)
        os.remove(pdf_output_file)
        return False

    return True

#generate_thumb(sys.argv[1])