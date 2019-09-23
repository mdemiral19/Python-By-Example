'''Ask the user to enter number between 10 and 20 (inclusive). If they enter a number within tis range, display the message "Thank you",
otherwise display the message "Incorrect answer".'''

num1 = float(input('Please enter a number equal or higher than 10 and equal and lower than 20: '))
if num1 >= 10 and num1 <= 20:
    print('Thank you.')
else:
    print('Incorrect answer.')