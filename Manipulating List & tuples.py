Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Manipulating List
L2=['Tailor swift','Ed Shreen','Imagine Dragons','Pink Floyd','Marron 5']
L2.append('Hashley')
L2
['Tailor swift', 'Ed Shreen', 'Imagine Dragons', 'Pink Floyd', 'Marron 5', 'Hashley']
L2.insert('One Direction')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    L2.insert('One Direction')
TypeError: insert expected 2 arguments, got 1
L2.insert(0,'One Direction')
l2
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    l2
NameError: name 'l2' is not defined. Did you mean: 'L2'?
L2
['One Direction', 'Tailor swift', 'Ed Shreen', 'Imagine Dragons', 'Pink Floyd', 'Marron 5', 'Hashley']
L1=['Java','Python','C++']
L1.remove('C++')
L1
['Java', 'Python']
L1.pop()
'Python'
L2.reverse()
L2
['Hashley', 'Marron 5', 'Pink Floyd', 'Imagine Dragons', 'Ed Shreen', 'Tailor swift', 'One Direction']
L2.sort()
L2
['Ed Shreen', 'Hashley', 'Imagine Dragons', 'Marron 5', 'One Direction', 'Pink Floyd', 'Tailor swift']
L2.sort(reverse=True)
L2
['Tailor swift', 'Pink Floyd', 'One Direction', 'Marron 5', 'Imagine Dragons', 'Hashley', 'Ed Shreen']
\
l1=['Hi','hello','Whatsapp']
tuple(l1)
('Hi', 'hello', 'Whatsapp')
t1=('Python','java','C++')
list(t1)
['Python', 'java', 'C++']
