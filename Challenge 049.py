'''Create a variable called compnum and set the value to 50. Ask the user to enter a number. While their guess is not the
same as the compnum value, tell them f their guess is too low or too high and ask them to have another guess. If they enter
the same value as compnum, display the message "Well done, you took [count] attempts."'''

number = int(input('Enter a number: '))
compnum = 50
count = 1
while compnum != number:
    if compnum > number:
        print('The number is too low.')
    else:
        print('The number is too high.')
    count = count + 1
    number = int(input('Have another guess: '))
print('Well done, you took', count, 'attempts.')