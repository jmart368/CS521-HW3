"""
Name: Jose Martinez
Class: CS 521 - 2020 Spring 1
Date: 9 February 2020
Homework Problem # 5.3
Description: Converting kilograms to pounds
"""

# create your varaibles for kilograms and pounds where 1 lb = 2.2 kl
kilograms = 1
pounds = 2.2
# fromat your header for kilograms, allow space to align with the numbers
print('{0}   {1}'.format('Kilograms', 'Pounds'))
# invoke the while loop ro repeat the loop up to 200
# format the print statment of the loop and format the print of the ouput
# the += 2 will allow odd numbers to be displayed
while kilograms < 200:
    print('{0:9d} {1:8,.1f}'.format(kilograms, kilograms * pounds))
    kilograms += 2
