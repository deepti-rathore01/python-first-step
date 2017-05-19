"""
@ file   : list.py
@brief   : Check the 'n' and 'l' is available or not in 'gnu'
@authore : deepti
@date    : 18-5-17

"""
list = ['gnu']
a = raw_input("enter the input to check in the list")
print a
if a in list: print "the input is there",a
else:
    print "it is not there"

