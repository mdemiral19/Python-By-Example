'''Challenge 042: Set a variable called total to 0.
Ask the user to enter five numbers and after each input ask them if they want that number included.
If they do, then add the number to the total. If they don't want it included, don't add it to the total.
After they have entered all five numbers, display the total.'''

variable = 0
for i in range(0, 5):
    num = int(input('Enter a number: '))
    question = input('Do you want to add this number? Please answer writing either \'yes\' or \'no\': ')
    if question == 'yes':
        variable = variable + num
print(variable)
