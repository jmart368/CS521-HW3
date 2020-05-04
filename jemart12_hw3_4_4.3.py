"""
Name: Jose Martinez
Class: CS 521 - 2020 Spring 1
Date: 9 February 2020
Homework Problem # 4.3
Description: Solve for a linear equations
"""

import sys

# prompt the user to enter values seprated using split as a seprator
user_input = input("Enter numerical values for a, b, c, d, e, f seperated "
                   "a coma: ").split(",")

# prompt the user to enter exactly 6 numerial values, capture the exception
if len(user_input) != 6:
    print("You must enter 6 numbers seperated by commas. Try Again.")
    sys.exit()

# make sure the user uses float numbers only, caputre the exception
for float_numbers in range(len(user_input)):
    try:
        user_input[float_numbers] = float(user_input[float_numbers])
    except ValueError:
        print("{} is not a float! Try again".format(user_input[float_numbers]))
        sys.exit()

# define your variables with user_input to validate your formulas
a, b, c, d, e, f = user_input

# use if to capture the 'no solution" print if the result is 0
if a * d - b * c == 0:
    print('The equation has no solution')

# use else to capture the results of the two linear equations
else:
    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d-b * c)
    print("x is", x, "and y is", y)
