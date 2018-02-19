"""
@file  : list_comprehension.py
@brief : Print odd number between 1-100 using list comprehension
"""
a = range(1,100)
b = [x for x in a if x%2 != 0]
print "odd number between 1 to 100:",b

