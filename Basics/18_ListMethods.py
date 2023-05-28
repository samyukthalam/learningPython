numbers=[4,2,8,45,10,0,1,0]
numbers[2]=88 # Modify a specific value at an index
print(numbers[2])

numbers.append(20) # append value at the end
print(numbers)

numbers.insert(0,80) # Insert value at a specified index
print(numbers)

numbers.pop() # Remove the last item
print(numbers)

print(numbers.index(45)) # Print the index of a given value

print(numbers.count(0)) # Count the occurence of an item in the list

numbers.remove(45) # Removes a specific value from the list
print(numbers)

numbers.sort() # Sorts the list
print(numbers)

numbers.reverse() # Reverses the List
print(numbers)

numbers2=numbers.copy()
print(numbers2)

numbers.clear() # Empty the list
print(numbers)

# REMOVE DUPLICATES IN A LIST

dupe_nums = [3,5,45,8,1,0,2,8,4,77,100,100,2,10]
unique_nums=[]
for num in dupe_nums:
    if num not in unique_nums:
        unique_nums.append(num)
print(unique_nums)

# PRINT THE INDEX OF REPEATED NUM IN THE LIST
name = 'Swathi Samyuktha Lam'
nameToList=[x for x in name]  # List Comprehension
plist = list(dict.fromkeys(nameToList)) # A dictionary cannot have duplicates
for char in plist:
    count_Of_Each_Char=nameToList.count(char)
    print(f"count of {char} is {count_Of_Each_Char}")
