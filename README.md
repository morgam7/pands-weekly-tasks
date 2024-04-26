# Weekly Tasks Repository

This is the repository containing all the weekly tasks for the Programming and Scripting module of the [Higher Diploma in Science in Data Analytics given by ATU Galway-Mayo](https://www.gmit.ie/higher-diploma-in-science-in-computing-in-data-analytics). My lecturer was [Andrew Beatty](https://github.com/andrewbeattycourseware?tab=overview&from=2022-12-01&to=2022-12-31). Each week he set us the task of writing a simple python program using the new skills we had learnt.

To create this repository, I installed Python using [Anaconda](https://www.anaconda.com/download), and I used [Visual Studio Code](https://code.visualstudio.com/) as a text editor and terminal.

## Week 1: Hello World!

We had to write a program that printed the words Hello World!

## Week 2: bank.py

We had to write a program that inputs and adds up two integers.

The tricky part of this week's task was understanding the difference between strings, ints and floats and how they affect functions. The input function automatically inputs as a string. I needed to put 'int' before input to specify that it was an integer so that I could use the addition function to add up the amounts. I thought I needed to specify that that answer be returned as a float so that I could get a decimal, but it automatically does this. 

However, when I went to print my answer with the text "The sum of these is $ " with '+ answer' I wasn't able to because the program "can only concatenate str (not "float") to str". So I had to use the format method. This also allowed me to specify that I wanted to return two decimal places so that for answers ending with a zero it kept the zero.

Also, I had to use the dollar sign because I couldn't find the euro sign on my keyboard. New laptop!

Links that helped this week:

https://www.geeksforgeeks.org/python-data-types/ \
https://www.w3schools.com/python/python_datatypes.asp \
https://stackoverflow.com/questions/20449427/how-can-i-read-inputs-as-numbers \
https://www.w3schools.com/python/ref_string_format.asp \
https://stackoverflow.com/questions/15619096/add-zeros-to-a-float-after-the-decimal-point-in-python

## Week 3: accounts.py

We had to write a program that inputs an account number and replaces all but the last 4 numbers with an X.

So the solution involved returning a section of a string. I researched how to use the slice function on a string. Negative slicing can be used to slice a string from the end back. So this would work for an account number of any length. However, this did not work for me when I tried it. I found a great explanation [here](https://stackoverflow.com/questions/13672627/why-does-my-negative-slicing-in-python-not-work) for why and was able to correct my syntax.

However, this would still print 6 X's before the last four digits of the account number no matter how many numbers preceded the last 4 numbers of the account number. I did some research on how to replace each digit before the last 4 with X but this involved some complicated concepts I don't understand yet. The replace() function might work here.

Links that helped this week:

https://www.w3schools.com/python/python_strings_slicing.asp \
https://www.w3schools.com/python/python_strings.asp \
https://stackoverflow.com/questions/13672627/why-does-my-negative-slicing-in-python-not-work \
https://www.freecodecamp.org/news/python-string-replace-how-to-replace-a-character-in-a-string \
https://stackoverflow.com/questions/30141233/replacing-the-integers-in-a-string-with-xs-without-error-handling \
https://www.askpython.com/python/string/python-replace-function 


## Week 4: collatz.py

We had to write a program that inputs any positive integer and outputs the successive value by taking the current value. 
and, if it is even, dividing it by two, but if it is odd, multiplying it by three and adding one. The program continues until the last value is one.

The first thing I had to do here was create a list. The first number of this list would be the inputted integer. Then I used the while, if and else functions to create the other numbers in the list. I had difficulty in fuguring out how to close the loop and ended up getting infinite loops that I had to stop by hitting ctrl+C. Thankfully Andrew showed us how to do this! 

The thing I ended up being most confused about this week was this: '(number % 2) == 0' 
I got this piece of code from Andrew's tutorial and initially I thought that it just meant the number was divided (%) by 2. But of course % means remainder not divide and what the peice of code is saying is that when the number is divided by 2 the remainder is 0. This misunderstanding caused me problems becasue I went on to use '%' instead of '/' to divide, which did not work out well!

Another problem I had was that When I got the program to output the list I wanted it didn't print 1 as the last number. I realised that this was becasue 1 would not be added to the list becasue, as per the while loop instructions, a newnubmer would only be added if greater than one. So I had to add 1 to the list after the loop had closed.

The other issue I had was that the values were not outputting onto the same line. Couldn't figure out how to do this until someone else posted the same problem to the slack channel and I got the solution there. You have to use 'end = " "'

Links that helped this week:

https://www.geeksforgeeks.org/python-lists/ \
https://www.geeksforgeeks.org/what-is-a-modulo-operator-in-python \
https://www.w3schools.com/python/python_while_loops.asp \
https://realpython.com/python-while-loop 

## Week 5: weekday.py

We had to write a program that tells you whether today is a weekday.

I found this week's task easy, though I may have only done so becasue I avoided using lists. I used the if, elif, else function instead. 

I googled how to import the day of the week and loads of links came up for the datetime library which was very straighforward to use.

So this week was an easy one.

Links that helped this week:

https://stackoverflow.com/questions/32032504/python-time-greeting-program \
https://www.w3schools.com/python/python_datetime.asp \
https://docs.python.org/3/library/datetime.html 

## Week 6: squareroot.py

We had to write a program that inputs a positive floating point number and finds the square root.

This week was not so easy. 

So the first thing I did was write the struction of the function. I started out with a simple calculation so I could get the syntax right. When I had the structure of the function working then I was able to fill in the more complicated squareroot calculation.

As Andrew suggested I used Newton's method to get the squareroot, which looked complicated but was simple really when broken down. I found loads of suggestions online for code. I used the random.uniform function to get the initial guess squareroot but I soon realised that I could have used any number here. The other code I saw online set it to '1' usually. So I was getting a bit unnecessarily fancy with using random.

It all seemed to be going well until I got this error message that said: ZeroDivisionError: division by zero. I couldn't figure out where I'd gone wrong and thought it had something to do with using random.uniform for the guessroot. But it turned out that I had mistakenly written the if clause as (number - approxroot) instead of (guessroot - approxroot). This is why I kept getting the endless recursion.

Finally I used the format function to round the answer to two decimal places.

Links that helped this week:

https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method \
https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository \
https://en.wikipedia.org/wiki/Newton%27s_method \
https://www.geeksforgeeks.org/random-numbers-in-python \
https://www.geeksforgeeks.org/python-randint-function \
https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method \
https://www.w3schools.com/python/ref_func_abs.asp \
https://www.w3schools.com/python/ref_random_uniform.asp 

## Week 7: es.py

We had to write a program that reads in a txt file and counts the number of e's in it.

This week I used a lot of code that I don't quite understand but it seems to work.

First I practiced opening a file using code from Andrew's lectures. 

Then I figured out how to count 'es' by gooling: How do you count the number of es in a text file? I found out that you can use the count() function and it was very straight forward.

Then to figure out how to input the file from the command line I googled this line from the weekly task description: "The program should take the filename from an argument on the command line." And I found a link that gave me code using argparse. 

The last thing to do was to download the mobydick.txt file. I found one on github but it is only the first volume so when I run the program I get 58820 es as opposed to the 116960 es that Andrew got.

This week seemed very easy but it feels like I somehow managed to get the program to work without really understanding why it does.

Links that helped this week:

https://stackoverflow.com/questions/18647707/count-letters-in-a-text-file \
https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python \
https://www.pythonforbeginners.com/argparse/argparse-tutorial \
https://docs.python.org/3/library/argparse.html#core-functionality 

## Week 8: plottask.py

We had to write a program that displays (1) a histogram of a normal distribution of 1000 values with a mean of 5 and standard deviation of 2, and (2) a plot of the function h(x)=x3 in the range 0 to 10, on the one set of axes.

For the last week's task I got familiar with using numpy and matplotlib.pyplot, which was very useful for the other projects that we are doing this semester. I used numpy to generate the datasets and then matplotlib.pyplot to generate the plots. 

This was acutally straighforward enough but I complicated it by mis-reading the task's instructions. I thought the two datasets had to be related so that I had to cube the 1000 randomly generated values (Maybe this was exactly what we had to do! I'm still not sure) and plot that dataset. This caused loads of problems because I got a mental looking plot with the line zigzaging back over itself like a scribble. This scribble plot happened becasue the plotting function will go from value to value in the array (which was made up of random numbers) so if I wanted a nice clean line I needed to order the x value array from smallest to largest. I could not figure out how to do this. I tried to use sorted() but it didn't work. 

Eventually I re-read the instructions and I used a completely different dataset to generate the x values for the second plot. I used numpy.array and was able to specify the range.

After doing that, plotting the datasets was simple enough and I used code from Andrew's labs to make the plots look nice.

Links that helped this week:

https://www.geeksforgeeks.org/how-to-plot-a-normal-distribution-with-matplotlib-in-python \
https://www.w3schools.com/python/numpy/numpy_random_normal.asp \
https://www.askpython.com/python/built-in-methods/cubing-numbers-python \
https://numpy.org/doc/stable/reference/generated/numpy.arange.html \
https://realpython.com/python-sort \
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html 



# End
















