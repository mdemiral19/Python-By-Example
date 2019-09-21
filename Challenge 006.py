'''Ask how many slices of pizza the user started wit and ask how many slices they have eaten. Work out how many slices they
have left and display the answer in a user-friendy format.'''

pizzastart = int(input('How many pizza slices did you have in the beginning?: '))
pizzaend = int(input('How many pizza slices have you already eaten?: '))
answer = pizzastart - pizzaend
print('You have', answer, 'pizza slices left. I hope you enjoyed the pizza. :-)')