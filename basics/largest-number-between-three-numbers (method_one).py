# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 22:24:08 2024

@author: Joyraz Barua
"""

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))

if (x>y) & (x>z):
    print(x,"is the largest number")
elif (y>x) & (y>z):
    print(y,"is the largest number")
else:
    print(z,"is the largest number")