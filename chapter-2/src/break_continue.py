"""
@ file   : break_continue.py
@ breif  :the program to break the loop if user give 'n' as input, if 'y' continue
@ authore : deepti
@ date : 18-5-17

"""
while True:
    name = raw_input("Enter your name >>>")
    age = input("enter your age >>>")
    employid = ("enter your id")
    mangername  = raw_input("enter your manager name")
    print name
    print age
    print employid
    print name
    a = raw_input("Want to enter more y/n >>>")
    if a is "n":
    #using 'break' to come out from loop
        break
    else:
        continue


