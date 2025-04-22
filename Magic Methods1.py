#Magic Methods 
class Employee:
    def __new__(cls):
        print("__new__ magic method is executed.")
        inst=object.__new__(cls)
        return inst
    def __init__(self):
        print("__init__ magic method is executed.")
        self.name="Saquib"
e1=Employee()
print(e1.name)