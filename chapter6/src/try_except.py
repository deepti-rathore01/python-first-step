""""
@ file  :try_expect.py
@brief  :Print 'Can not divide.' when 100/0
"""
try:
    a = 100/0
except ZeroDivisionError:
    print "can not divide"
