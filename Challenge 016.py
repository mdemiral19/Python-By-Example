'''Ask the user if it is raining and and convert their answer to lower case so it doesn't matter what case they type it in.
If they answer "yes", ask if it windy. If they answer "yes" to this second question, display the answer "It is too windy for an umbrella",
 otherwise display the message "Take an umbrella". If they did not answer yes to the first question, display the answer "Enjoy your day".'''

rainy = input('Is it raining?: ')
rainy = str.lower(rainy)
if rainy == 'yes':
    windy = input('Is it windy?: ')
    windy = str.lower(windy)
    if windy == 'yes':
        print('It is too windy for an umbrella.')
    else:
        print('Take an umbrella.')
else:
    print('Enjoy your day.')
