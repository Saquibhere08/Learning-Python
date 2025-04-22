#Using arguments with default values
def verdict(m1,m2,m3,m4=15000):
    total=m1+m2+m3
    if total>=m4:
        print("Yes, You can buy a new smartphone!")
    else:
        print("Sorry, This is not the right time to splurge on a smartphone.\n")
    return
gift=int(input("Gift Money from Family: Rs. "))
saving=int(input("Savings: Rs. "))
internship=int(input("Internship,raened with sweat and blood: Rs. "))
verdict(gift,saving,internship,10000)
