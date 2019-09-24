'''Challenge 021: Ask the user to enter their first name and then ask them o enter their surname.
Join them together with a space between and display the name and the length of the whole name.'''

firstname = input('Please enter your first name: ')
surname = input('Please enter your surname: ')
fullname = firstname + " " + surname
length = len(fullname)
print(fullname)
print(length)