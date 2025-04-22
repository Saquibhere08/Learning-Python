age=7
def a():
    print("Global variable 'age': ",globals()['age'])
    #Now modifying the global variable 'age' INSIDE the function
    globals()['age']=20
    print("Global variable 'age' modified INSIDE the function: ",globals()['age'])
    
    #Now creating a local variable, 'age' INSIDE the function.
    age=11
    print("Local variable 'age': ",age)
    return
a()
print("Checking global variable OUTSIDE the function: ",age)