"""
@file : sub_string.py
@brief:counting the sub sting from the given string
"""
def my_sub_string_count(string):
    count = 0
    for i in range(len(string)):
        if string[i] =='c' and string[i+1] =='o' and string[i+3] == 'e' :
              count += 1
    return count


string = raw_input("enter string\n")
count = my_sub_string_count(string)
print count

