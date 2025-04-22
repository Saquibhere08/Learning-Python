#program on elif
# Check if a year is a leap year and print the message, "This is a leap year". If it is a leap year.
year=int(input("Enter the Year: "))
if (year//100):
    print("This is a Leap Year")
elif (year//4):
    print("This is not a Leap Year.")
    