# collatz.py
# A program that inputs any positive integer and outputs the successive value by taking the current value 
# and, if it is even, dividing it by two, but if it is odd, multiplying it by three and adding one. 
# The program continues until the last value is one.
# Author: Marcella Morgan

numbers = []
number = int (input ("Please enter a positive integer: "))   
while number > 1:
    numbers.append(number)
    if (number % 2) == 0:
        newnumber = int (number / 2)
    else: 
        newnumber = int (number * 3 + 1)
    number = newnumber
for value in numbers:
 print (value, end = " ")





'''
# WORKING IT OUT:


# So first I need to do 'if elif else' to deal with the different calculations for odd and even numbers.
# So the even numbers calculation:

#number = int (input ("Please enter a positive integer: "))
#if (number % 2) == 0:
#    print (int (number / 2))
#else: 
#    print ( "You have entered a very odd number.")

# took ages to figure this out. Couldn't figure out why I needed the '== 0' or it won't understand the code. I didn't 
# realise that this '(number % 2) == 0' is how you write an even number. I thought that you just needed to say if the
# number is divisible by 2 (number %2) [thinking that % meant divided by] that's enough but no of course you need to say that the remainder is 0.
# So then it wasn't dividing for me but the reason it wasn't dividing was I was using the % to divide. But the % is
# to get percentage. I need / to divide!

# also I was trying to just do the if part first to see if it was working but the whole code won't work without the else bit.


# Ok so now the odd numbers calculation:

#number = int (input ("Please enter a positive integer: "))
#if (number % 2) == 0:
#    print (int (number / 2))
#else: 
#    print (int (number * 3 + 1))   

# Ok so now the loop. 
# I need to tell it to keep doing this until the number is 1.

#number = int (input ("Please enter a positive integer: "))   
#while number > 1:
    #if (number % 2) == 0:
        #print (int (number / 2))
   # else: 
        #print (int (number * 3 + 1))  

# So many infinite loops! Had to figure out how to change the input so that it wouldn't keep looping:
        
#number = int (input ("Please enter a positive integer: "))   
#while number > 1:
#    if (number % 2) == 0:
#        newnumber = number / 2
#    else: 
#        newnumber = number * 3 + 1
#    print (int(newnumber))
#    number = newnumber

# So now can I figure out how to put them all on the same line or do we need to do this? If I write it as a list?

#numbers = []
#number = int (input ("Please enter a positive integer: "))   
#while number > 1:
#    numbers.append(number)
#    if (number % 2) == 0:
#        newnumber = number / 2
#    else: 
#        newnumber = number * 3 + 1
#    number = newnumber
#for value in numbers:
# print (int(value))


# Nope still on different lines. Will have to leave it there.

# Saw post on slack channel that gave solution!
 
#numbers = []
#number = int (input ("Please enter a positive integer: "))   
#while number > 1:
#    numbers.append(number)
#    if (number % 2) == 0:
#        newnumber = int (number / 2)
#    else: 
#        newnumber = int (number * 3 + 1)
#    number = newnumber
#for value in numbers:
# print (value, end = " ")


'''



