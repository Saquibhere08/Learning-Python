def SayHello(name): #(name) - Formal argument
    "This function will display a greeting message"
    print("Hello! {}.Welcome.\n".format(name))
    return
you=input("Enter your name: ")
SayHello(you)
friend=input("Enter your friend's name: ")
SayHello(friend) #'you','friend' -Actual arguments