'''Challenge 034: Display the following message:

"
1) Square
2) Triangle

Enter a number:
"

If the user enters 1, then it should ask them for the length of one of ts sides and display the area.
If they select 2, it should ask for the base andheight of the trianlge and display the area. If they type in anything else,
it should give them a suitable error message.'''

import math
print('1) Square\n2) Triangle')
num = int(input('Please enter either 1 or 2 according to your desired calculation: '))
if num == 1:
    side = float(input('Please enter the side, preferably in cm: '))
    area = side**2
    print('The area of the square is', area)
elif num == 2:
    height = float(input('Please enter the height, preferably in cm: '))
    base = float(input('Please enter the base, preferably in cm: '))
    area = 0.5 * height * base
    print('The area of the triangle is', area)
else:
    print('Wrong option, this operation is not possible. Please choose either 1 or 2.')