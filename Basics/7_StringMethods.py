name = 'Swathi Samyuktha Lam'
len_of_name=len(name) #length of the string
print('The length of the string ' + name + ' is ' + str(len_of_name))
print('String in upper case ' + name.upper())
print('String in lower case ' + name.lower())
is_decimal = name.isdecimal()
print('Is the String decimal?? '+ str(is_decimal))
print('String in capitalized format ' + name.capitalize())
print('Find the index of L in the string ' + str(name.find('L')))
name=name.replace('Lam','Nukathoti')
print('Name after replace is ' +name)
print('Swathi' in name) #check if the name has a particular string
print('S' in name) #check if the name has a particular char