'''Challenge 031: Ask the user to enter the radius of a circle (measurement from the centre point to the edge). Work
out the area of the circle.'''

import math
radius = float(input('Please enter the radius of a circle, preferably in cm: '))
circlearea = math.pi * (radius**2)
print('The circle area is', circlearea)