names=["swathi","Sam","Lam"]
name1,name2,name3=names
print(f"unpacked names are {name1} {name2} {name3}")

numbers=(13,6,1,7)
num1,num2,num3,num4=numbers
print(f"Unpacked numbers are {num1} {num2} {num3} {num4}")

t = (0, 1, 2, 3, 4)
a, b, *c = t
print(a)
print(b)
print(c)