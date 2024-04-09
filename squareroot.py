# squareroot.py
# A program that inputs a positve floating point number and finds the square root.
# Author: Marcella Morgan

# First I'm going to write the function:

def squareroot(number, guessroot):  
    
    # Newtons square root method: Guess the square root. (Will input this later) Then divde the original number by 
    # the guess square root and add to guess square root. Then divide this number by two.
    approxroot = 0.5 * (guessroot + (number/guessroot))

    # Keep doing this until the difference between your successive answers are less than the tolerance limit.
    if (guessroot - approxroot) < 0.00000000000001: #(this is the tolerance limit)
        return approxroot
    else:
        return squareroot(number, approxroot) 
        # using the function with approxroot here to continue looping fucntion with successive answers.

    
# Now to input the arguments:

number = float (input("Please enter a positive number: " )) # Must specify float as otherwise inputted as string

# For the guess root using random to create a random 'guess'. (Could have used any number between 1 and number.) 
# Must use random.uniform function to create a float
import random
guessroot = random.uniform(1, number)
ans = squareroot(number, guessroot)
print (f"The square root of {number} is approx. {ans}.")

'''
# Working it out: (Very messy becasue I decided to try to write the code after just watching first lecture. Just to see
# how far I could get.)

# So first the easy bit: ask for the input number.

print (input("Please enter a positive number: "))

# Ok so now how to do the hard bit. I need to create a function that finds the squreroot of a number.
# So I will create a function using def. Will fugrue out how to do this with simple multiply first - just want to 
# figure out function first.
# need to define the input mumber as number so first line need to change. 
# Also this will have to be an int becasue it will input as a string.
 

number = int (input("Please enter a positive number: " ))
def squareroot (number):
    return (number * 3)
print return

# nope can't make it just print return have to define return as ans?

number = int (input("Please enter a positive number: " ))
def squareroot (number):
    ans = (number * 3)
print (f"{ans}")

# nope nope not working back to drawing board. Geting ans not deifned. Not understanding fucntions yet. Will watch more lectures.

# But before that going to take quick look at newtons square root method: So it goes like - First approximate the square root. Then divde the original number by the approximate 
# square root and add to appoximate square root. Then divide this number by two. Keep doing this until the difference between
# your sucessive answers are less than the tolerance limit.
# Okay so was thinking how the hell do you tell the computer to approximate a square root?! But the approximate can be
# any mumber. And then you keep doing it untill you get closer to the actual square root. So you just need to tell
# the computer to enter a random number. It can be any nubmer. Doesn't have to be close to right. But needs to be less than the 
# nubmer entered

# So I need to import the random function and then get it to choose a random number from 0 - inputted value.


number = int (input("Please enter a positive number: " ))
import random
guessroot = random.randint(0, number)
print (guessroot)

# ok so I have a random number as the guess square root. Now to do the maths. 

number = int (input("Please enter a positive number: " ))
import random
guessroot = random.randint(0, number)
squareroot = 0.5 * (guessroot + (number / guessroot))


#Have no idea what I'm doing here. and his won't work. And should be using fucntions. But! can I do this with an if else? Just 
# going to put in 0.01 for the tolerence


if (number - squareroot) < 0.01:
    print (squareroot)
else:
    closersquareroot = 0.5 * (squareroot + (number / squareroot))
    closersquareroot = squareroot

# okay no none of this is working. Need to look at more lectures. 


# okay so after looking at lectures going to go back to creating a fucntion first so the initial attempt at this. So lets 
# do this with simpler function - back to very basic


number = int (input("Please enter a positive number: " ))
def squareroot (number):
    return number * 3
ans = squareroot(number)
print (ans)

So:

number = int (input("Please enter a positive number: " ))

# so this is the part I need to change
def squareroot (number):
    return number * 3
# when I change this part I get a different answer - this is where I insert the more complicated squareroot function

ans = squareroot(number)
print (ans)

# okay so I have this simple function working so now to do the complicated squareroot fucntion.



# okay so back to defining the squareroot function. Doing the first part:

def squareroot (number):
    import random
    guessroot = random.randint(0, number)
    return squareroot = 0.5 * (guessroot + (number / guessroot))

# will this work? Let's see

number = int (input("Please enter a positive number: " ))
ans = squareroot(number)
print (ans)


# oh no can't do that with the return - get rid of the squareroot.

def squareroot (number):
    import random
    guessroot = random.randint(0, number)
    closersquareroot = 0.5 * (guessroot + (number / guessroot)))

# will this work? Let's see

number = int (input("Please enter a positive number: " ))
ans = squareroot(number)
print (ans)


# i think this is working but I'm not sure. Now I need to get the function to keep running until it reaches the tolerance
# limit. How to do this? This is where I use if else? how to work this out? Using exemple code from here:
# https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
# Will this work?? 

def squareroot (number):
    import random
    guessroot = random.randint(0, number)
    0.5 * (guessroot + (number / guessroot))

    if (number - squareroot) < 0.000001:
    return squareroot

else:
return squareroot (number)
    

# Lets see:

number = int (input("Please enter a positive number: " ))
ans = squareroot(number)
print (ans)

# nope need to fix syntax


def squareroot (number):
    import random
    guessroot = random.randint(0, number)
    0.5 * (guessroot + (number / guessroot))

    if (number - squareroot) < 0.000001:
        return squareroot
    else:
        return squareroot(number)
    

# Lets see:

number = int (input("Please enter a positive number: " ))
ans = squareroot(number)
print (ans)

# nope need the closersquareroot defined:


def squareroot(number):
    import random
    guessroot = random.randint(0, number)
    approxsquareroot = 0.5 * (guessroot + (number/guessroot))

    if (number - approxsquareroot) < 0.000001:
        return approxsquareroot
    else:
        return squareroot(number)
    

# Lets see:

number = int (input("Please enter a positive number: " ))
ans = squareroot(number)
print(ans)

# arrghhh so many errors!But i'm close. Why am I getting this: ZeroDivisionError: division by zero. What does that mean?
# looked it up at some stage I'm dividing by zero which gives infinity and computer can't compute infinity so 
# is it the random number here? Do i need to change the 0 to 1? try that

def squareroot(number):
    import random
    guessroot = random.randint(1, number)
    approxsquareroot = 0.5 * (guessroot + (number/guessroot))

    if (number - approxsquareroot) < 0.000001:
        return approxsquareroot
    else:
        return squareroot(number)
    

# Lets see:

number = int (input("Please enter a positive number: " ))
ans = squareroot(number)
print(ans)

# oh noooooo it's got something to do with the recursion - so this random number thing might not be working.
# Or need to change the argument that goes into the function at the else clause?

def squareroot(number):
    import random
    guessroot = random.randint(0, number)
    approxsquareroot = 0.5 * (guessroot + (number/guessroot))

    if (number - approxsquareroot) < 0.000001:
        return approxsquareroot
    else:
        approxsquareroot = number
        return squareroot(number)
    

# Lets see:

number = int (input("Please enter a positive number: " ))
ans = squareroot(number)
print(ans)


# nooo the problem is with the random. The nubmer doesn't need to be random duh! I can just put in any number. 1 - just 
put in guessnumber as 1 everytime.

# okay so after looking at more lectures my issue might be how the arguments are inputted.
# I can define the guessroot outside the fuction might be better

def squareroot(number, guessroot):
    approxsquareroot = 0.5 * (guessroot + (number/guessroot))

    if (number - approxsquareroot) < 0.000000000000001:
        return approxsquareroot
    else:
        return squareroot(number, approxsquareroot)
   

# When I went to input a float it wouldn't work because I had imported random ints. 
# Had to change to random.universal function

number = float (input("Please enter a positive number: " ))
import random
guessroot = random.uniform(1, number)
ans = squareroot(number, guessroot)
print (f"The square root of {number} is approx. {ans}.")


# Nope still not working - getting recursion going on for too long. Over and Over. Don't understand why. Need to look 
# at lectures again

# Okay so I figured out why it wasn't working. After all that! it was because I had the if clause as (number - approxroot)
# instead of (guessroot - approxroot)!! hours spent futhering around with code and it was just that stupid mistake i kept
# copying over and over!!! Argggh! Can't believe that was all it was.


def squareroot(number, guessroot):
    approxsquareroot = 0.5 * (guessroot + (number/guessroot))

    if (guessroot - approxsquareroot) < 0.000000000000001:
        return approxsquareroot
    else:
        return squareroot(number, approxsquareroot)


number = float (input("Please enter a positive number: " ))
import random
guessroot = random.uniform(1, number)
ans = squareroot(number, guessroot)
print (f"The square root of {number} is approx. {ans}.")

'''