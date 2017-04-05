# PDF 2 JPG ...

Repository created to allocate utility.py module

### Utility.py ...

Code which extracts the first page from a pdf file and converts it 2 jpg

### How To ...

For this example we have used a ubuntu64 machine by vagrant software:
 
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-pip python-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev libjpeg8-dev zlib1g-dev libmagickwand-dev
sudo apt-get update
sudo apt-get upgrade
sudo pip install -r requirements
```

These commands will install all necessary to run utility.

### Step By Step ...

These are the steps made to make it happen:

* Open PDF & Extract 1st Page (PyPDF2)
* Write 1st Page 2 PDF File (PyPDF2)
* First Page PDF 2 JPG (wand.image)

Before any exception a message will appear


### Test It ...

This Repository includes test file to verify right functionality:

```
python test.py
test_utility (__main__.TestUtilityMethods) ...
FILE "fichero.txt" NOT FOUND ...

FILE "/home/vagrant/test.pdf" NOT FOUND ...
ok

----------------------------------------------------------------------
Ran 1 test in 2.416s

OK

```

Just notice the existence of the following files:

* descarga.pdf

### Try It ...

```
python
Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:24:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from utility import generate_thumb
>>>
>>>
>>> generate_thumb("prueba.txt")

FILE "prueba.txt" NOT FOUND ...
False
>>> generate_thumb("descarga.pdf")
True
>>> quit()

```

If return value is True you´ll obtain jpg file with the same name than parameter in "generate_thumb"

