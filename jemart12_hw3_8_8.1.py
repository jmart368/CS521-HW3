"""
Homework Problem # 8.1
Description: Entering valid SSN using functions
"""


def main():
    """Invoke a function prompting user to enter social in given format. Use
    .strip method to remove spaces at the beginning and end of the string."""
    s = input('Enter a Social Security number in ddd-dd-dddd format: ')\
        .strip()

    def checksnn(s):
        """Create a function that capture exceptions for the user entering
        the numbers. Ensure that the exact digits are captured using len."""
        if(len(s)) != 11:
            return False

        # check the range of digits entered testing the numbers range
        for i in range(0, 3):
            if not s[i].isdigit():
                return False
        for i in range(4, 6):
            if not s[i].isdigit():
                return False
        for i in range(7, len(s)):
            if not s[i].isdigit():
                return False

        # invoke an if/else statement to check that - are placed correctly
        if s[3] != '-' and s[6] != '-':
            return False
        else:
            return True

    if checksnn(s):
        """Call back the check function, check for alignment"""
        print('valid ssn')
    else:
        print('invalid ssn')


main()
"""Call back the main function, when using ensure that functions are align
or else the code will not work. It will run only"""
