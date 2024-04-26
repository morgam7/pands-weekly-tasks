# plottask.py
# A program that displays (1) a histogram of a normal distribution of 1000 values with a mean of 5 and standard deviation of 2,
# and (2) a plot of the function h(x)=x3 in the range 0 to 10, on the one set of axes.
# Author: Marcella Morgan




# First I'm going to import the libraries that I need:
import numpy as np
import matplotlib.pyplot as plt
from numpy import random

np.random.seed(1) 
# Using random function that lets me set the mean and the standard deviation. 
# Also going to seed the random nubmer so that I will always get the me numbers when i run it
x = random.normal(loc=5, scale=2, size=(1000))

xpoints = np.array(range(0,10))
ypoints = xpoints**3

plt.plot(xpoints, ypoints, color='r', label="xpoints cubed") # need to put in label so that the legend will work
plt.hist(x, label="normal distribution of 1000 values")


# Making the plot pretty by adding code from andrew's lab tutorial:
plt.title("Plot task")
plt.xlabel("x values")
plt.ylabel("y values")
plt.legend()
plt.show()





'''
# WORKING IT OUT:

# First I'm going to import the libraries that I need:

import numpy as np
import matplotlib.pyplot as plt
from numpy import random


# So before I do the plots I need to get the values. So I have two sets of values to get. First:
# (1) 1000 values - normal distribution with mean 5 and standard deviation 2
# Got code from this site: https://www.w3schools.com/python/numpy/numpy_random_normal.asp
# Going to use the random fucntion that lets me set the mean and the standard deviation
# Also going to seed the random nubmer so that I will always get teh same numbers when i run it as covered in lab.







np.random.seed(1)
x = random.normal(loc=5, scale=2, size=(1000))

print(x)
'''
# Okay so that seem to be working. I'm getting an array of 1000 random numbers anyway. So I will need to do a 
# histogram with these x values.

# So second set of values:
# a plot of the function h(x)=x3 in the range 0 to 10.
# Ok so this isn't an array of values. I'm using the x values I've just generated and cubing them and plotting that.
# Okay so is it just that y=x3? The h in h(x)=x3 is throwing me but I think it's just simply saying that y is x3.
# Okay so I'll see if I can print those values.

# Forgot how to cube. This tutorial useful:https://www.askpython.com/python/built-in-methods/cubing-numbers-python
# So ** followed by numbers of times you want to multply get any to the power of.
'''

np.random.seed(1)
x = random.normal(loc=5, scale=2, size=(1000))
y = x**3 
print(x)
print (y)

'''




# Okay so that worked I've got my two sets of values to now I need to plot them.

#First we'll plot the numbers cubed. Going to use this code I copied from labs:

'''
xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints #multiply each entry by itself
plt.plot(xpoints, ypoints)
plt.show()



# But I've already got the values so lets see if I can just do this:

plt.plot(x, y, color='r') # Adding code from Andrew's lab tutorial here to make the line red
plt.show()
'''



# Okay so I got a plot but it's a mental looking one. The line is zigzaging back over itself so it looks like a scribble.
# Also defo does not look like a normal distribution. But would it look like a normal distibution? - no of course not
# Becasue the y value will go up as the x value goes up of course. Its the historgram that will have the bell curve.
# This scribble plot happened in Ian's tutorial going to watch that again and see what he does. 
# Okay so Ian got the scirbbles doing a scatter plot but the reason it's happening here is that I need to order the 
# x value array from smallest to largest becasue the plotting fucntion will go from value to value in the array. 
# I need to order the x values.
# So how to do that?? Real pyton to the rescue https://realpython.com/python-sort/,
# Need to use sorted function and it's defaul is ascending order

'''
np.random.seed(1)
x = random.normal(loc=5, scale=2, size=(1000))
sortedx = sorted(x)
y = x**3 
print(sortedx)
print (y)
'''

# Okay so that is sorting the x axis in ascending order. But y values are still random but that won't matter. This should work.
# But I've just noticed I'm getting negative vlaues. Not sure if this matters. It doesn't say on weekly task description that 
# numbers need to be positive. But it does say that that the range of values of the y axis needs to be 0-10.
# So when i'm genertatin the y vlaues I need to sepecify that i want only those values in that range.
# Don't know if this will work but giving it a shot
'''
np.random.seed(1)
x = random.normal(loc=5, scale=2, size=(1000))
sortedx = sorted(x)
y = x**3(range(0,10))
print(sortedx)
print (y)

'''

# Nope that didn't work. Maybe I can do the range when I sort the x numbers

'''
np.random.seed(1)
x = random.normal(loc=5, scale=2, size=(1000))
sortedx = sorted(x)range(0,10)
y = x**3
print(sortedx)
print (y)


# nope didn't work either. So going to try this again with the y numbers. Got this "for x in range "code from here: 
# https://numpy.org/doc/stable/reference/generated/numpy.arange.html 

np.random.seed(1)
x = random.normal(loc=5, scale=2, size=(1000))
sortedx = sorted(x)
y = x**3 for x in range(0,10)
print(sortedx)
print (y)

# nope try with square brackets?
np.random.seed(1)
x = random.normal(loc=5, scale=2, size=(1000))
sortedx = sorted(x)
y = [x**3 for x in range(0,10)]
print(sortedx)
print (y)

'''

# That kind of worked. So I'm getting closer but only have 10 values in y. So yeah that just made it retun 10 values. Not sure what I'm doing here.
# Need to leave it. Will come back to it.
# No wait now - what it's done is it has rturned the cube of all the 9 ints up to 10. So the range function must reutrn ints. Can I get it
# to return floats?
'''
np.random.seed(1)
x = random.normal(loc=5, scale=2, size=(1000))
sortedx = sorted(x)
y = x**3
'''

# nope doesn't work have to come back to it.

# Okay so a bit more research online and found this: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html
# So i think I can specify the limits of the y axis. Btu I'll need to do this while writing the code for the plot. So 
# going to do that:

'''
plt.plot(sorted(x), y, color='r') 
plt.ylim((0, 10))
plt.show()
'''

# Oh no disaster got a crazy graph that looked like blood dripping down the screen.
# Going to get rid of the ylim to see what happens

'''
plt.plot(sorted(x), y, color='r') 
plt.show()

# Now it's looking like the standard deviaton bell curve but done with lines. So it's just plotting the x axis.
# Ah yes of course! the y axis is cubing a different set of numbers - the xsorted array. Oh and also I had it plot
# sorted(x) instead of sortedx

np.random.seed(1)
x = random.normal(loc=5, scale=2, size=(1000))
sortedx = sorted(x)
y = sortedx**3

plt.plot(sortedx, y, color='r') 
plt.show()

# It won't let me do the cube function on sortedx. But what if I go back one step and maybe it was just becasue I had
# the sorted(x) instead of sortedx

np.random.seed(1)
x = random.normal(loc=5, scale=2, size=(1000))
sortedx = sorted(x)
y = x**3

plt.plot(sortedx, y, color='r') 
plt.show()

# No still not working. Very frustrating. I'm getting further away from the answer. Why won't it let me cube sortedx?
# both x and sortedx are arrays. Why are they being treated differently?

print (x)
print (sortedx)

# Ok so I'm going to get rid of the sorted x and do the ylim

np.random.seed(1)
x = random.normal(loc=5, scale=2, size=(1000))
y = x**3

plt.plot(x, y, color='r') 
plt.ylim(0,10)
plt.show()

# nope another crazy looking graph. Ok so lets try it with limiting x values. That would make more sense
np.random.seed(1)
x = random.normal(loc=5, scale=2, size=(1000))
y = x**3

plt.plot(x, y, color='r') 
plt.xlim(0,10)
plt.show()

# Okay so back to the plot looking fairly ok but still have a scribble effect. Going to try it again wiht sortedx

np.random.seed(1)
x = random.normal(loc=5, scale=2, size=(1000))
y = x**3
sortedx = sorted(x)

plt.plot(sortedx, y, color='r') 
plt.xlim(0,10)
plt.show()

# Nope going around in circles here. 
# Oh wait maybe what andrew is looking for is two different set of numbers! That Im cubing the standard distribution array.
# But what he wants is just a simple y=x3 generating these with a much simpler function!
# Okay I'm just going to do that then becasue I can't work it out the other way

np.random.seed(1)
x = random.normal(loc=5, scale=2, size=(1000))

xpoints = np.array(range(0,10))
ypoints = xpoints**3


plt.plot(xpoints, ypoints, color='r', label="xpoints cubed") # need to put in label so that the legend will work
plt.hist(x, label="normal distribution of 1000 values")



# Making the plot pretty by adding code from andrew's lab tutorial:


plt.title("Plot task")
plt.xlabel("x values")
plt.ylabel("y values")
plt.legend()
plt.show()
'''