'''Ask the user for their name and their age. Add 1 to their age and display the output
[Name] next birthday you will be  [new age]' '''

name = str(input('What\'s you\'re name?: '))
age = int(input('How old are you?: '))
newage = age + 1
print('Hello', name, 'next year you\'ll be', newage, 'years old.')