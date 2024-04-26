
# bank
# program that inputs and adds up two integers
# Author Marcella Morgan

amount1 = int (input("Enter amount1(in cent): ")) 
amount2 = int (input("Enter amount2(in cent): "))
# Must specify that it is an int or will automatically input as a string and so will not add up the amounts.

answer = format((amount1 + amount2) /100,'.2f')
# Will automatically turn int to float when divided by 100.
# Using format so will always return two decimal places and not drop the zero when answer ends in zero.

print (f"The sum of these is ${answer}")
# Had to use a more complicated syntax here because you can't concatenate a float to a string. 





