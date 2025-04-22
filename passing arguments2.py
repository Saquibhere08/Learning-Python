#modifyning the passing arguments
def myfunction(newlist):
    newlist.append(60)
    print("Modified list inside function: ",newlist)
    return

mylist=[10,20,30,40,50]
print("List before passing to function: ",mylist)
myfunction(mylist)
print("List after passing to function: ",mylist)
