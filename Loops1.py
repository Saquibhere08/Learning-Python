#Loops "while"
#defining variables
day=0
squats=0
total=0
print("Enter the no. of squats you did on each day: ")

#while loop and the loop body
while day<=6:
    day=day+1
    squats=int(input("Squats on Day {}".format(day)))
    total=total+squats

#statements outside of the while loop
avg=total/day
print("In the last {} days, you did an average of {} squats".format(day,avg))