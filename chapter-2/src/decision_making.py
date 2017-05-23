"""
@ file    : decision_making
@ brief   : simple program to understand the loops
@authore  : deepti
@date     : 17-may-17

"""

a = input("enter the value for a\n")
b =input("enter the value for b\n")
if (a == b):
    print "a is equal to b"
    print a
    print b

else: print "not equal"
#while loop
count =0
while count<5:
    print count, "is less than 5"
    count = count+1
else:
    "count is not less then 5"
#for loop
fruit =["apple", "mango", "banana"]
for fruits in fruit:
    print"fruits in list:",fruits

#break statement
i = 10
while i > 0:
    print"value of i is:",i
    i =i-1
    if i ==5:
        break
#continue statement
i = 10
while i > 0:
    i =i-1
    if i == 5:
        continue
    print "value of i",i
        
