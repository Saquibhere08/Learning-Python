#Taking money from sister to pay dues
#If the num<7000 show "Ahem,can you rethink the numbers please?"
#If the num>10000 display "WOW! sis you are a queen"
#If the number is in within the range than show "Cool, Thanks sis x rupees certainly help"
def checkmoney(x):
    if  x in range(7000,10001) :
        print("Cool,Thanks sis! {} rupees will certainly help".format(x))
    elif x<7000:
        print("Ahem, Can you rethink the number please?")
    elif x>10000:
        print("Wow sis! You are a queen")

    return

sis=8500
checkmoney(sis)