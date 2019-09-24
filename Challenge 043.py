'''Challenge 043: Ask which direction the user wants to count (up or down).
If they select up, then ask them for the top number nd then count from 1 to that number.
If they select down, ask them to enter a number below 20 and then count down from 20 to that number.
If they entered something other than up or down, display the message "I don't understand.'''

direction = input('Do you want to count up or down? Either enter \'up\' or \'down\': ')
if direction == 'up':
    topnumber = int(input('Please enter a number: '))
    for i in range(0, topnumber + 1, 1):
        print(i)
elif direction != 'up':
    downnumber = int(input('Please enter a number below 20: '))
    for i in range(20, downnumber - 1, -1):
        print(i)
else:
    print('I don\'t understand.')
