'''Task the user to enter a number over 100 and then enter a number under 10 and tell them how many times
the smaller number goes into the larger number in a user-friendly format.'''

number1 = int(input('Please enter a number over 100: '))
number2 = int(input('Please enter a number under 10: '))
answer = number1 / number2
print(number2, 'goes', answer, 'times into', number1)