names=['swathi','Sam','Anil','Smaran','Saanvi','Prateek','Angel','Ramya']
for name in names:
    print(name)
print(names[0])
print(names[1])
print(names[2])
print(names[3])

print(names[-1]) # Last
print(names[-2]) # Last but one

print(names[1:]) # all from the second word
print(names[0:-1]) # First to last but one

# Find the largest number in a list
numbers=[5,7,1,0,22,57,34,10]
largestnum=0
for num in numbers:
    if num>largestnum:
        largestnum=num
print(largestnum)

