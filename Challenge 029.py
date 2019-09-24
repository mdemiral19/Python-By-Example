'''Challenge 029: Ask the user to enter an integer that is over 500. Work out the square root of that number and display it to two
decimal places.'''

import math
number = float(input('Enter a number over 500: '))
if number > 500:
    print(math.sqrt(number))
else:
    print('Nice try!')