"""
@ file  : countletter.py
@ brief : Print the letters from 'gnu-linux is rule the world now
@ authore : deepti
@date : 18-may-17

"""

for letter in 'gnu-linux is rule the world now':
    if (((letter >= "a") or(letter >= "A")) and ((letter >= "z") or (letter >="Z"))):
        print 'letter :',letter
