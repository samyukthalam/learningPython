number=input("Enter a number >> ")
numToWordDict={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
}

output=""

for ch in number:
    output+=numToWordDict.get(ch,"!")+" "
print(output)

