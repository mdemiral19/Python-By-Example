'''Challenge 036: Alter program 035 so that it will ask the user to enter their name and a number and then display their
 name that number of times.'''

name = input('Please enter your name: ')
num = int(input('Please enter a number: '))
for i in range(0, num):
    print(name)
