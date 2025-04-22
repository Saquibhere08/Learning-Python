#else with the while loop
x=0
while x<=5:
    x=x+1
    print("This is iteration no {} in the 'while' loop".format(x+1))
else:
    print("This is the else block in the loop.")
print("Now, the loop ends.")