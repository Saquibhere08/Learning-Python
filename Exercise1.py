#Program on if-else statements
#Write a program to check if a number is positive and print message,"This is a positive number"
num=int(input("Enter any Number"))
if (num>0):
    print("This Number is Positive")
else:
    if(num<0):
        print("This number is Negative")
    else:
        if(num==0):
            print("Number is neither Positive nor Negative")
        else:
            print("-----Invalid Number-----")
