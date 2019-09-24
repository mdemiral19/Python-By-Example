'''Challenge 041: Ask the user to enter their name and a number.
If the number is less than 10, then display their name that number of times; otherwise display the message "Too high" three times.'''

name = input('Please enter your name: ')
number = int(input('Please enter a number: '))
if number < 10 and number > 0:
    for i in range(0, 3):
        print(name)
else:
    print('Too high value.')
