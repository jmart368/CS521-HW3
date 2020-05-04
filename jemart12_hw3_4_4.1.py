"""
Homework Problem # 4.1
Description: Solve for the following quadratic formula ax**2 + bx + c = 0
"""

import math
import sys

# prompt the user to enter values for a, b, c
# validate the exact number of prompts usingh 'if len' and 'sys.exit()'
user_input = input("Enter three numbers for a, b, c sperated by a comma:")\
    .split(",")
if len(user_input) != 3:
    print("You must enter 3 numbers seperated by commas. Try again.")
    sys.exit()

# validate the float exceptions using try and except
for float_number in range(len(user_input)):
    try:
        user_input[float_number] = float(user_input[float_number])
    except ValueError:
        print("{} is not a float! Try again.".format(user_input[float_number]))
        sys.exit()

# asign a, b, c as user_input so that these variables are defined in formulas
a, b, c = user_input

# create a variable for the discriminant equation
discriminant = (b**2) - (4 * a * c)

# invoke the if statetment if the discriminant is greater than 0
# format your answers
if discriminant > 0:
    radius1 = (-b + math.sqrt(discriminant)) / (2 * a)
    radius2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("The roots are ", format(radius1, ".6f"), "and ",
          format(radius2, ".6f"))

# invoke elif if the discriminant is equal to 0
elif discriminant == 0:
    x = -b / (2 * a)
    print("The root of the equation is ", x)
# invoke else if the condition is false and the equations has no roots
else:
    print("The equation has no roots")
