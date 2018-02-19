"""
@file   :double_character
@brief  :Given a string, return a string where for every char in the original, t         here are two chars.
         Eg.   double_char('The') = 'TThhee'
"""
a = raw_input("give a string for doubling the character")

def fun(a):
    print " doubling the string character"

    return "".join([x*2 for x in a])

print fun(a)

