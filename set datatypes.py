Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Set Datatype
s1={1,"Saquib",75.50}
s1
{1, 75.5, 'Saquib'}
type(s1)
<class 'set'>
s2={10,20,30,43,50,10}
s2
{50, 20, 10, 43, 30}
#set() Function
s1=set("Internshala")
s1
{'n', 'I', 'l', 'e', 'r', 's', 'h', 'a', 't'}
s2=set([45,67,87,36,55])
s2
{67, 36, 45, 87, 55}
s3=set((10,25,15))
s3
{25, 10, 15}
#add() in set
s1=set({"Python","Java","C++"})
s1
{'Python', 'C++', 'Java'}
s1.add("Perl")
s1
{'Perl', 'Python', 'C++', 'Java'}
#update()
s1={"Python","Java","C++"}
s1.update(["C++", "Basic"])
s1
{'Basic', 'Python', 'C++', 'Java'}
s1.clear()
s1
set()
#copy()
s1={"Python","Java","C++"}
s2=s1.copy()
s2
{'Python', 'C++', 'Java'}
s1={"Python","Java","C++"}
s1.discard("Java")
s1
{'Python', 'C++'}
#remove()
s1={"Python","Java","C++"}
s1.remove("C++")
s1
{'Python', 'Java'}
