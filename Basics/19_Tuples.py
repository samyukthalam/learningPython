# Tuples are immmutable - you cannot change a tuple

numbers=(2,4,1)
print(numbers[0])

# numbers[0]=10 this throws am error

nums=(1,2,3,(5,6)) # Nested Tuple
num1,num2,num3,num4=nums
print(f"Unpacked tuples are {num1} {num2} {num3} {num4[0]} {num4[1]}")
