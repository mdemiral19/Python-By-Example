'''Challenge 032: Ask for the radius and the depth of a cylinder and work out the total volume (circle area*depth) rounded to
three decimal places.'''

import math
radius = float(input('Please enter the radius of a cylinder, preferably in cm: '))
depth = float(input('Please enter the depth of a cylinder, preferably in cm: '))
area = math.pi * (radius**2)
cylindervolume = area * depth
print('The cylinder volume is', round(cylindervolume,3))