# Print each character in a String
for char in 'Swathi Samyuktha Lam':
    print(char)

for word in ['Swawthi','Samyuktha', 'Lam']:
    print(word)

for num in [4,1,0,210]:
    print(num)

for number in range(5): # does not include the last index
    print(number)

for item in range(5,10,2): # prints 5 then skip 2 numbers, print 7 and skip 2 numbers
    print(item)

item_Prices=[10,20,30]
total=0
for price in item_Prices:
    total+=price
print(total)
