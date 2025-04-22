class person:
    counter=0 #Class Attribute-Shared by all functions
    def __init__(self, a='SAquib bin Halim',b='MAle'): #__init__ method is invoked everytime an object is created from the class.
        self.name=a #Attributes or Instance variables
        self.gender=b #Attributes or Instance variables
        person.counter=person.counter+1
    def Showinfo(self): #In Python whenever we are creating an method in a class we have to pass the argument 'self'.
        print('Name: ', self.name)
        print('Gender: ', self.gender)
    @classmethod
    def ShowCount(cls): #class method
        print('Number of objects created so far: ',cls.counter)
    
#Class Method are callable by class and not by an individual object. You Add '@classmethod' before every class method and you pass the argument 'cls' instead of 'self' in the class method.
        
