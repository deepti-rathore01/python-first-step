"""
@file  : odd_even.py
@brief : deepti
@authore: deepti
@date: 22-may-17
"""
a = input("enter the value for range")
list1 = []
for loop in range(a):
    list2  = input("")
    list1.append(list2)

print "value for list",list1
even = []
odd = []
for i  in range(a):
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

print "even:",even
print "odd:",odd
