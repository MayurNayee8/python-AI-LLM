'''

how to read file
how to write in file
how to append data in file

file 

mode

r - read
r+ = read and write
a - append
w - write (override)
w+ - write and read


read() - all data raed
readline() - one line 
readlines() - read all lines in and retuen in list
'''
import os

file = open("/Users/apple/Desktop/maypython_AILLM/.venv/prompt.txt","r")
filedata = file.read()
print(filedata)

file = open("/Users/apple/Desktop/maypython_AILLM/.venv/prompt.txt","r+")
data = file.readline()
print(data)

'''
fileappend = open("/Users/apple/Desktop/maypython_AILLM/.venv/prompt.pdf","a")
fileappend.write("new line")
fileappend.close
'''

with open("/Users/apple/Desktop/maypython_AILLM/.venv/prompt.pdf", "r") as data3:
    data4 = file.read()
    print(data4)