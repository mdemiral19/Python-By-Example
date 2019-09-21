'''Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of
diners and show how much each person must pay.'''

totalprice = int(input('How much is the total price of the bill: '))
diners = int(input('How many diners are there?: '))
singlepayment = totalprice / diners
print('Each person has to pay', singlepayment)