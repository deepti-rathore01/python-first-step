"""
@file : graph.py
@brief :Write a program to count no of lines in n no of text files and
        Plot it as a bar graph as File vs Lines.
"""
import os
import fun
import matplotlib.pyplot as plt 

a = input("enter number of file you want to open\n")
c = []
d =[]
for loop in range(a):
    b = raw_input("enter the name of files which you want to open\n")
    d.append(b)

    num=fun.count_line(b)
    print "number of lines=",num
    c.append(num)
list1 = [ n for n in range(a)]
plt.bar(list1, c , align ="center")
plt.xticks(list1,d)
plt.show()



