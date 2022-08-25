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
stdout.write (str (number)+"\n")
