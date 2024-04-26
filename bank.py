# bank
# program that inputs and adds up two integers
# Author Marcella Morgan

amount1 = int (input("Enter amount1(in cent): ")) 
amount2 = int (input("Enter amount2(in cent): "))
# Must specify that it is an int or will automatically input as a string and so will not add up the amounts.

answer = (amount1 + amount2) /100
# Will automatically turn int to float when divided by 100.

print ("The sum of these is $", format(answer, '.2f'))
# Had to use a more complicated syntax here because you can't concatenate a float to a string. 
# This syntax will also always return two decimal places.




