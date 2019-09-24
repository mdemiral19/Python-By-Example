'''Challenge 039: Ask the user to enter a number between 1 and 12
and then display the times able for that number.'''

num = int(input('Please enter a number between 1 and 12: '))
if num > 1 and num < 12:
    for i in range(0, 12):
        print(i * num)
else:
    print('Please follow the correct instructions. ')

# alternatively
'''
num = int(input('Please enter a number between 1 and 12: '))
if num > 1 and num < 12:
  for i in range (0,12):
    answer = i*num
    print(i, 'x', num, '=', answer)
else:
  print('Please follow the correct instructions. ')
'''
