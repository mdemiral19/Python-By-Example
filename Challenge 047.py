'''Ask the user to enter a number and then enter another number. Add these two numbers together and then ask if they want
to add another number. If they enter 'y', ask them to enter another number and keep adding numbers untl they do not answer 'y'.:
Once the loop has stopped, display the total.'''

num1 = float(input('Please enter a number: '))
total = num1
again = 'y'
while again =='y':
    num2 = float(input('Please enter another number: '))
    total = total + num2
    again = input('Do you want to add another number? (y/n): ')
    print('The total number is', total)