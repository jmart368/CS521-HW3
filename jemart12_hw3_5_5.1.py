"""
Name: Jose Martinez
Class: CS 521 - 2020 Spring 1
Date: 9 February 2020
Homework Problem # 5.1
Description: Solve for 2 linear equations
"""

# declare variables
positives = 0
negatives = 0
total = 0
average = 0.00

# run the process until user enters the zero
while True:
    number = int(input("Enter an integer, the input ends if it is 0:"))
    # break if user enters the value zero
    if(number == 0):
        break
    # otherwise if the user enters values
    else:
        # calculate total
        total = total + number
        # count negative numbers
        if(number < 0):
            negatives = negatives + 1
        # count positive numbers
        else:
            positives = positives + 1

# check whether the user enters aleast a number or not
if(positives == 0 and negatives == 0):
    print("You didn\'t enter a number.")
else:
    # create a formula for the average
    average = total / float(positives + negatives)
    print("The number of positives is", positives)
    print("The number of negatives is", negatives)
    print("The total is", total)
    print("The average is", average)
