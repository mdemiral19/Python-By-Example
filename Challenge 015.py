'''Ask the user to enter their favourite colour. If they enter "red", "RED" or "Red", display the message "I like red too",
otherwise display the message "I don't like [colour. I prefer red".'''

colour = input('What\s your favourite colour?: ')
if colour == 'Red' or colour == 'RED' or colour == 'red':
    print('I like red too.')
else:
    print('I don\'t like', colour,'. I prefer red.')