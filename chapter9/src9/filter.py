"""
@file : filter.py
@brief :Filter the string elements from data = [100, '200', 'gnu', 0] using filt        er() with help of lambda and type functions
"""

data = [100,'200','gnu',0]
data = filter(lambda data: type(data) == str,data)
print data
