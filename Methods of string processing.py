Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Methods of string processing \
#capitalize()
var='Saquib'
var.capitalize()
'Saquib'
var='saquib'
var.capitalize()
'Saquib'
var.upper()
'SAQUIB'
var.lower()
'saquib'
#title()\
var='python training from internshala'
var.title()
'Python Training From Internshala'
var.find('in')
10
var.find('on')
4
var.find('run')
-1
# index()
var.index('in')
10
var.index('run')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    var.index('run')
ValueError: substring not found
#count()
var.count('in')
3
# isalpha()
var='Internshala'
var.isalpha()
True
num='Intern Shala'
num.isalpha()
False
#isdigit()
var='2000'
var.isdigit()
True
var='20,000'
var.isdigit()
False
#islower()
var='internshala'
var.islower()
True
var.islower()
True
var='INTERNSHALA'
var.issupper()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    var.issupper()
AttributeError: 'str' object has no attribute 'issupper'. Did you mean: 'isupper'?
var.isupper()
True
