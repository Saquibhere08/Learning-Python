#program for 'if' & 'else'condition statement
price=int(input("Enter the price of donut: Rs. "))
quantity=int(input("Enetr the no. of donuts: "))
amount=price*quantity

if amount>1000: #if statement is used
    print("Yaya...a discount of 10% is applicable")
    discount=amount*10/100
    amount=amount-discount

#if the amount is less than Rs.1000,5% is discount
else:
    print("A discount of 5% is applicable")
    discount=amount*5/100
    amount=amount-discount
print("Total Amount is Rs. ",amount)

 
