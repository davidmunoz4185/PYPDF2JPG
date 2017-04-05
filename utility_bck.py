import os
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter
from wand.image import Image


def get_filename(path):
    """

    """
    filename = os.path.splitext(path)[0]
    return os.path.basename(filename)


def get_path(path):
    """

    """
    local_path = os.path.dirname(path)
    if local_path != '':
        return local_path
    else:
        return "."


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
        print "FILE \"{one}\" NOT FOUND ...".format(one=path)
        return False
    except:
        print "ERROR READING \"{one}\" BY \"PdfFileReader\" ...".format(one=path)
        return False

    #pdf_orig_name = get_filename(path)
    #pdf_orig_path = get_path(path)
    pdf_output_file = "{one}_{two}.pdf".format(one=path,
                                               two="1stPage")
    outputStream = file(pdf_output_file, "wb")

    # Write 1st Page 2 PDF File
    try:
        pdf_output.write(outputStream)
        outputStream.close()
    except IOError:
        print "ERROR CREATING FIRST PAGE FILE \"{one}\" ...".format(one=pdf_output_file)
        return False

    jpg_output_file = "{one}.jpg".format(one=pdf_orig_name)
    jpg_output_file = os.path.join(pdf_orig_path, jpg_output_file)

    # Save PDF as JPG 283 x 400
    try:
        with Image(filename=pdf_output_file) as img:
            img.resize(283, 400)
            img.save(filename=jpg_output_file)
            os.remove(pdf_output_file)
    except:
        print "ERROR CREATING JPG FILE \"{one}\" ...".format(one=jpg_output_file)
        os.remove(pdf_output_file)
        return False

    return True

#generate_thumb(sys.argv[1])