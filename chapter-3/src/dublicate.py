"""
@file : dublicate.py
@brief:the program to remove the duplicate elements from list
@authore : deepti
@date : deepti
"""

a = input("enter the value for range")
list1 = []
for loop in range(a):
    list2  = input("")
    list1.append(list2)
    print "value for list",list2
list1 = list(set(list1))
print list1


