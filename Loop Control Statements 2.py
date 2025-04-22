#check for a prime number
num=int(input("Enter a Number: "))
for x in range(2,num):
    if num%x== 0:
        print("{} is NOT a prime number.".format(num))
        break
else:
    print("{} is a prime number.".format(num))
    