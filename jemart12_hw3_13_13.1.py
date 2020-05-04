"""
Homework Problem # 13.1
Description: Removing text from a text file
"""

# prompt users to enter files in txt format
file_name = input('Enter filename format in .txt format: ')
s = input('Enter the string to be removed: ')

try:
    # read all the data from file first
    f = open(file_name)
    data = f.readlines()
    f.close()

    # open same file in write mode now
    f = open(file_name, 'w')

    # replace the strings
    for d in data:
        f.write(d.replace(s, ''))
        f.close()
        print('Done')
# create an exception message for incorrect format
# use a test file to see that the word is deleted
except ValueError:
    print('unable to find input file.')
