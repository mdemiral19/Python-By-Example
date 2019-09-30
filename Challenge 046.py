'''Ask the user to enter a number. Keep asking until they enter a value over 5 and then display the message
"The last number you entered was [number]" and stop the program.'''



num = 0
while num <= 5:
    num = float(input('Please enter a number: '))
    print('The last number was', num)