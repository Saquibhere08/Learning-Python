#Let's build a Calculator (a+b), (a-b) , (a*b), (a*b), (a/b), (a%b) 
# Mini project

first=input("Enter First Number : ")
operator=input("Enter operator(+,-,8,/,%) : ")
second= input("Enter second Number: ")

first =int(first)
second =int(second)
if operator == "+" :
    print(first + second)
elif operator == "-" :
    print(first - second)
elif operator == "*" :
    print(first * second)
elif operator == "/" :
    print(first / second)
elif operator == "%" :
    print(first % second)

else:
    print("------Invalid Number------")