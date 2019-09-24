'''Challenge 025: Ask the user to enter their first name. If the length of their first name is under five characters,
ask them to enter their surname and join them together (without a space) and display the name in upper case.
If the length of their first name is five or more characters, display their first name in lower case.'''

firstname = input('Please enter your first name: ')
lengthfirstname = len(firstname)
if lengthfirstname < 5:
    surname = input('Please enter your surname: ')
    fullname = firstname + surname
    print(fullname.upper())
else:
    print(firstname.lower())
