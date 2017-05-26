"""
@file   :count_line.py
@brief  :Write a program to count no of lines in a text file.
"""
def count_line(fname):

    num_lines = 0
    with open(fname, 'r') as f:
        for line in f:
            num_lines += 1
    return num_lines

fname = raw_input("Enter file name: ")
num_lines = count_line(fname)
print("Number of lines:")
print(num_lines)
