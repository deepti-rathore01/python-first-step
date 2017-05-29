"""
@file: commandline.py
@brief: "Get the 5 numbers from command line and do the basic arithmetic operations. First argument should be like 'add', 'mul'. Do the operatio         ns based first argument word."
"""
import sys
c = int(sys.argv[2])
if sys.argv[1] == "add":
    for i in range (2, len(sys.argv)):
        c = c + int(sys.argv[i])
        print c
elif sys.argv[1] == "mul":
    for i in range (2,len(sys.argv)):
         c = c* int(sys.argv[i])
    print c
                    
elif sys.argv[1] == "sub":
    for i in range (2,len(sys.argv)):
        c = c- int(sys.argv[i])
    print c

elif sys.argv[1] == "div":
    for i in range (2,len(sys.argv)):
        c = c/ int(sys.argv[i])
    print c


