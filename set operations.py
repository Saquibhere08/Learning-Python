Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Set Operations
#Uniom
#Union*
#Union of two sets is a set of all elements in both.
s1={1,2,3,4,5}
s2={6,7,8,9}
s1|s2
{1, 2, 3, 4, 5, 6, 7, 8, 9}
s1.union(s2)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
#Intersections - Intersection of two sets is a set containing elements common to both.
s1&s2
set()
s1={1,2,3,4,5}
s2={6,7,8,9}
s1&s2
set()
s1.intersection(s2)
set()
s1={1,2,3,4,5}
s2={6,7,8,9}
SyntaxError: multiple statements found while compiling a single statement
s1={1,2,3,4,5}
s2{4,5,6,7,8}
SyntaxError: invalid syntax
s1={1,2,3}
s2(2,3,4)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s2(2,3,4)
TypeError: 'set' object is not callable
s2{4,5,6}
SyntaxError: invalid syntax

#symmetric difference
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s1^s2
{1, 2, 3, 6, 7, 8}
s1.symmetric_difference(s2)
{1, 2, 3, 6, 7, 8}
