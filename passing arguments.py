#Passing Arguments by Reference
def myfunction(newlist):
    print("list accessed in function: ","id",id(newlist))
    return
mylist=[10,20,30,40,50]
print("List before passing to function: ","id:",id(mylist))
myfunction(mylist)
