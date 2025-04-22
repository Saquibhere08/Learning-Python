Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#dictionary Datatype
iccpoints={'India':125,"South Africa":110,"England":105,"New Zealand":97}
iccpoints
{'India': 125, 'South Africa': 110, 'England': 105, 'New Zealand': 97}
#It can COinntain other datatypes:
points={"p1":[10,10],"p2":[20,20]}
#It has values such as list in keyvallue pairs.
items={("Parker","Reynolds","Camlin"):"Pen",("LG","Whirlpool","Samsung"):"Refigirator",("Dell","Acer","HP"):"Laptop"}
#In this dictionary objects the keys are tuples.
#key=immutable in Dictationnary
#Number,String and tuple can be used but not List as List is mutable
#get() Methods
capitals={"USA":"DC","India":"New Delhi"}
capitals
{'USA': 'DC', 'India': 'New Delhi'}
capitals.get("India")
'New Delhi'
points
{'p1': [10, 10], 'p2': [20, 20]}
items
{('Parker', 'Reynolds', 'Camlin'): 'Pen', ('LG', 'Whirlpool', 'Samsung'): 'Refigirator', ('Dell', 'Acer', 'HP'): 'Laptop'}
#Updating an Dictionary
iccpoints={'India':125,"South Africa":110,"England":105,"New Zealand":97}
iccpoints['India']=1300
iccpoints
{'India': 1300, 'South Africa': 110, 'England': 105, 'New Zealand': 97}
iccpoints['Astralia']=150
iccpoints
{'India': 1300, 'South Africa': 110, 'England': 105, 'New Zealand': 97, 'Astralia': 150}
#we ca aslo add more datas in the dictionary using the above code
