
"""
# File     : exercise1.py
# Brief    :A program for simple arithmetic operations like add, subtract, multiplication, division and etc
"""

a = input("enter a number for a \n")
b = input("enter a number for b  \n")

choice = raw_input( " enter the operation you want  \n")

if choice == 'add':
    print a+b
if choice == 'sub':
    print a-b
if choice == 'div':
    print a/b
if choice == 'multiplication':
    print a*b
if choice == 'mod':
    print a%b
if choice == 'exponent':
    print a**b



