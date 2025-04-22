Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
balltype='basketball'
result='hit'
'i wonder why the %s was getting bigger. Then it %s me.' %(balltype,result)
'i wonder why the basketball was getting bigger. Then it hit me.'
balltype='pumpkin'
'i wonder why the %s was getting bigger. Then it %s me.' (balltype,result)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    'i wonder why the %s was getting bigger. Then it %s me.' (balltype,result)
TypeError: 'str' object is not callable
'i wonder why the %s was getting bigger. Then it %s me.' %(balltype,result)
'i wonder why the pumpkin was getting bigger. Then it hit me.'
'i wonder why the %t was getting bigger. Then it %t me.' %(balltype,result)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    'i wonder why the %t was getting bigger. Then it %t me.' %(balltype,result)
ValueError: unsupported format character 't' (0x74) at index 18
