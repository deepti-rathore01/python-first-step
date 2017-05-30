"""
@file : sum.py
@brief : Calculating sum of numbers from 1-100 using reduce()
"""
a = reduce(lambda x,y:x+y, range(1,101))
print "the sum of range between 1 to 101 is :", a
