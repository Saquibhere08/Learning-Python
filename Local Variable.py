#local variables
age=7
def a():
    age=12
    print("Age is: ",age)
    return
a()
print("Age OUTSIDE the function: ",age)