#!/usr/bin/python3
from sys import stdout

orig = int (input ("Enter an integer: "))
number = orig
curdiv = 2
while curdiv < number:
    if (number%curdiv)==0:
        stdout.write (str (curdiv)+", ")
        number = number//curdiv
    else:
        curdiv = curdiv+1
if number==orig:
    stdout.write (str(number)+" is prime.\n")
else:
    stdout.write (str (number)+"\n")
