'''Challenge 022: Ask the user to enter their first name and surname in lower case. Change the case to title case
and join them together with a space between anddisplay the name and the length of the whole name.'''

firstname = input('Please enter your first name in lower case: ')
surname = input('Please enter your surname in lower case: ')
firstname = firstname.title()
surname = surname.title()
fullname = firstname + " " + surname
length = len(fullname)
print(fullname)
print(length)