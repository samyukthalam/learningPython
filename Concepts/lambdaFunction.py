# Print only positive numbers
given_list = [3,9,1,-3,-100,56,89]
new_list=list(filter(lambda x:x>0,given_list))
print(new_list)

# Double the argument
first_list=[1,2,3,4,5,6]
doubled_list=list(map(lambda x : x*2,first_list))
print(doubled_list)

