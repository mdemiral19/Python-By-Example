'''Ask the user to enter a number that is under 20. If they anter a nuber tht ist 20 or more, display the messsage
"Too high", otherwise display "Thank you.".'''

num1 = float(input('Enter a number under 20 please: '))
if num1 > 20:
    print('Too high.')
else:
    print('Thank you.')