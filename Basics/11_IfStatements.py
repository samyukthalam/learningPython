type_of_Day=input('Hows the day today >> ')
if type_of_Day == 'Hot':
    print('Drink plenty of water')
    print('Use Umbrella')
elif type_of_Day == 'Cold':
    print('Wear warmer clothes')
    print('Keep out of the snow')
else:
    print('Have a wonderful day')


house_Price=100000
buyer_Credit=input('What is your credit score >> ')
if buyer_Credit>str(800):
    downPayment=house_Price*0.1
else:
    downPayment = house_Price * 0.2
print('You should pay a down payment of ' + str(downPayment))
