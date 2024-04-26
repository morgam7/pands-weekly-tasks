# weekday.py
# A program that tells you whether today is a weekday.
# Author: Marcella Morgan

import datetime
x = datetime.datetime.now()
day = (x.strftime("%A"))
if day == "Saturday":
    print ("It is the weekend, yay!.")
elif day == "Sunday":
    print ("It is the weekend, yay!")
else:
    print ("Yes, unfortunately today is a weekday.")





'''
# WORKING IT OUT:

# So the two possible outputs are:


print ("Yes, unfortunately today is a weekday.")
print ("It is the weekend, yay!")



# now i need to fugure out how to return the right output given the day:
# Do I need to create two lists then? One for weekdays and one for weekends?

weekday = ("Monday", "Tuesday", "Wednesday", "Thrusday", "Friday")
weekend = ("Saturday", "Sunday")

# So then I need to tell it to read the inputted day and see what list it is in. If this day is in this
# list then print this. If not then print this. So only acutally need one list.

weekend = ("Saturday", "Sunday")

# So then do I need a list at all?

if day = "Saturday"
    print ("Yes, unfortunately today is a weekday.")
if day = "Sunday"
    print ("Yes, unfortunately today is a weekday.")
else
    print ("It is the weekend, yay!")


# Testing it. 
    
day = (input ("please enter a day:"))
if day = Saturday
    print ("Yes, unfortunately today is a weekday.")
if day = Sunday
    print ("Yes, unfortunately today is a weekday.")
else
    print ("It is the weekend, yay!")


# loads of syntax errors - need to use elif. need : after the if and else clause. Also only using on = sign
# means you are assigning not that it is equals to. Need to use ==. Need quotes around saturday and sunday.
# And had weekday output for weekends!



day = (input ("please enter a day:"))
if day == "Saturday":
    print ("It is the weekend, yay!.")
elif day == "Sunday":
    print ("It is the weekend, yay!")
else:
    print ("Yes, unfortunately today is a weekday.")




# Ok so now I need to figure out how to automatically input the day when the program is run.
# Looked online and the datetime function looks like it will work. 
# I can inport the date but I need the day to be displayed as a full word with a capital.
# And i want this to be consistent becasue the program wont' work unless the days are specifically in this format.
# I use the strftime function for this.

import datetime
x = datetime.datetime.now()
day = (x.strftime("%A"))
print (day)



# Okay so that worked. But lets see now if it'll do the if elif else stuff on it.

import datetime
x = datetime.datetime.now()
day = (x.strftime("%A"))
if day == "Saturday":
    print ("It is the weekend, yay!.")
elif day == "Sunday":
    print ("It is the weekend, yay!")
else:
    print ("Yes, unfortunately today is a weekday.")


# That worked yay!!!

'''

