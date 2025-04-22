# "for" loop for calculating the factorial
num=int(input("Enter a Number: "))
fact=1
for x in range(1,num+1):
    fact=fact*x
print("The Factorial of {} is {}".format(num,fact))