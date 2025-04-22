#global variables
age=7
def a():
    global age #global keyword
    age=12
    print("Age is: ",age)
    return
a()
print("Age OUTSIDE the function: ",age)