'''Challenge 023: Ask the user to type in the first line of a nursery rhyme and display the length of the string.
Ask for a starting number and an ending number and then display just that section of the text
(remember Python starts counting from 0 and not 1).'''

rhyme = input('Please enter the first line of a nursery rhyme: ')
lengthrhyme = len(rhyme)
print(lengthrhyme)
starting = int(input('Please enter a starting number: '))
ending = int(input('Please enter an ending number: '))
print(rhyme [starting:ending])
