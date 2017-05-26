"""
@file   :count_line.py
@brief  :Write a program to count no of lines in a text file.
"""
fname = raw_input("Enter file name: ")
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
         num_lines += 1
print("Number of lines:")
print(num_lines)
