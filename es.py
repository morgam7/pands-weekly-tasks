# es.py
# A program that reads in a txt file and counts the number of e's in it.
# Author: Marcella Morgan

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

with open(args.filename) as f:
    text = f.read()
    ans = text.count("e") 
    print (ans)


'''
# Working it out:

# SO first I'll practice opening a file using code given in lecture:

FILENAME = "test.txt"
with open(FILENAME, 'wt') as f:
    f.write("hello world2")

# When I run this a new file shows up in my weekly tasks repository. Ok so write creates the file and then writes the 
# text into it. Lets do read now:

FILENAME = "test.txt"
with open(FILENAME, 'r') as f:
    str =  f.read()
    print (str)

# ok so now I'm going to delete the file and then read it to see what happens. Yeah so no file there.
# ok so run the write file again and I'll see now if I can count the number of es in the test.txt.

# Adapting code I got from https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
# there is a count fucntion that will count letters. I need to define 'text' before I can use count. 'Text' is what is 
# read in test.txt.
    
  
FILENAME = "test.txt"
with open(FILENAME, 'r') as f:
    text = f.read()
    ans = text.count("e") # took a few tries to realise i had to put "" around e so it will be recognised as string
    print (ans)

# doing it now with l to see if defo working:

FILENAME = "test.txt"
with open(FILENAME, 'r') as f:
    text = f.read()
    ans = text.count("l") 
    print (ans)

# it works for test.txt. So now how do i import moby dick?
    
# Ok so I was confused about this instruction in the weekly task: "The program should take the filename
# from an argument on the command line." So i googled that line and found this:
# https://docs.python.org/3/library/argparse.html#core-functionality which is some info on argparse.
# so got this basic code from link here https://stackoverflow.com/questions/18862836/how-to-open-file-using-argparse
# No idea what I'm doing here but going to try to see if it works with test.txt


import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()
with open(args.filename) as f:
    text = f.read()
    ans = text.count("e") 
    print (ans)



# Oh my god it worked! I've no idea how that worked. The argparse stuff makes no sense to me but it worked. 
# so i can run this on text.txt from the command line


# So obviously if I type in moby-dick.txt into command line it will come back as file does not exist.
# Yeah I get this error: FileNotFoundError: [Errno 2] No such file or directory: 'moby-dick.txt'

# What happens if i try it with a .py file? It works! And with the README aswell.


# Ok so now I need to figure out how to get moby dick down as a file? And so do I then need to keep that
# file in my directory? 
    
# I'm going to see if I can create test.txt and also count the number of es in it running it from the command line.
    
filename = "test.txt"
with open(filename, 'wt') as f:
    f.write("hello world2")

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()
with open(args.filename) as f:
    text = f.read()
    ans = text.count("e") 
    print (ans)

# it worked!! So I don't need to keep the file in my depository. It will write the file. 
# But how do I get it to write moby-dick? Rather then writing text I'll need to import it? How do I do that?

# So I have downloaded mobydick.txt from an accoutn on github: https://gist.github.com/StevenClontz/4445774.
# So for now I am going to run this program from this downloaded moby dick file that is in my weekly tasks 
# repository.

# It might be possible to write a program that downloads this and creates a file for it in the depository and then 
# counts the es. In other words that it won't require having the txt file in the repository. 
# I'll look into this again if i have time.

'''
   






    
