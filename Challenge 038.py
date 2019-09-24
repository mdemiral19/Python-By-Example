'''Challenge 038: Change program 037 to also ask for a number. Display their name (one letter at a time on each line) and repeat
this for the number of times they entered.'''

name = input('Please enter your name: ')
num = int(input('Please enter a number: '))
for i in range(0, num):
    for i in name:
        print(i)
