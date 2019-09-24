'''Challenge 044: Ask how many people the user wants to invite to a party.
If they enter a number below 10, ask for the names and after each name display "[name] has been invited".
If they enter a number which is 10 or highe, dsplay the message "Too many people".'''

guests = int(input('How many guests do you want to invite to your party?: '))
if guests < 10 and guests > 0:
    for i in range(0, guests):
        name = input('Please enter the name of the guest: ')
        print(name, 'has been invited to your party!')
    print('Have fun everybody!')
else:
    print('Sorry, this doesn\'t seem to be a good idea.')
