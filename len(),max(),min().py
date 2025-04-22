Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#len()
L1=[12,5,6,7,8,3]
len(L1)
6
t1=(23,45,34,23,444,33,12,12)
len(t1)
8
#max()
max(L1)
12
max(t1)
444
#min()\
min(L1)
3
min(t1)
12
L5=['g',12,'r',45,43,8,'u',35]
t5=('one',2,'three',4,'five',6)
max(L5)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    max(L5)
TypeError: '>' not supported between instances of 'int' and 'str'
min(L5)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    min(L5)
TypeError: '<' not supported between instances of 'int' and 'str'
max(t5)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    max(t5)
TypeError: '>' not supported between instances of 'int' and 'str'
min(t5)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    min(t5)
TypeError: '<' not supported between instances of 'int' and 'str'
