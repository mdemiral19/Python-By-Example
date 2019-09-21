'''Ask the user to enter three numbers. Add together the first two numbers and then multiply this total by the third.
Display the answer as 'The answer is [answer]' '''

number1 = int(input('Enter a number please: '))
number2 = int(input('Enter a second number please: '))
number3 = int(input('Enter a third number please: '))
answer = (number1 + number2) * number3
print('The answer is', answer)