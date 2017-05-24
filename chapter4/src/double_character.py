"""
@file   :double_character
@brief  :Given a string, return a string where for every char in the original, t         here are two chars.
         Eg.   double_char('The') = 'TThhee'
"""
a = raw_input("give a string for doubling the character")
print a
print " doubling the string character"
print"".join([x*2 for x in a])


