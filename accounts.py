# accounts.py
# A program that inputs an account number and replaces all but the last 4 numbers with an X.
# Author: Marcella Morgan

# Inputting the account number. Input function automatically inputs as string.
accountno = (input("Please enter a 10 digit account number: "))

# Seperating the last 4 digits using slice function and printing the first 6 numbers as X's.
print ("XXXXXX" + (accountno[:-5:-1]))





'''
WORKING IT OUT:

# First input the account number. (Input function automatically inputs as string.)

accountno = (input("Please enter a 10 digit account number: "))

# Now I need to figure out how to seperate the last 4 digits. Use built in slice function?

print ("XXXXXX" + accountno[6:10])

# Now how to do this with a number of any length. Use negative indexing? 
accountno = (input("Please enter an account number: "))
print ("XXXXXX" + accountno[-10:-6])
# No duh of course that won't work!

accountno = (input("Please enter an account number: "))
print ("XXXXXX" + accountno[-1:-5])

# Still not working. Found out why here: https://stackoverflow.com/questions/13672627/why-does-my-negative-slicing-in-python-not-work
# I need to use a different syntax:

accountno = (input("Please enter an account number: "))
print ("XXXXXX" + accountno[:-5:-1])


# Can I figure out how to have the right amount of Xs? The program would need to count every number up to the 4th to last
# and then replace each number with an X.

# Getting numbers from 1st to 4th from last:

accountno = (input("Please enter an account number: "))
numbers_to_x = (accountno[0:-4])
print (numbers_to_x)

# Ok so now how do I replace the numbers in numbers_to_x with Xs???
# Looked up replace function but don't understand it yet. Will have to leave it here.

'''