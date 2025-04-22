class Employee:
    def __init__(self):
        self.name="Kiran"
        self.salary=100000
    def __str__(self): #str() is called
        return "Name= "+self.name+"Salary= "+str(self.salary)
e1=Employee()
print(e1)