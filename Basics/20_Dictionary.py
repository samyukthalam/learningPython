# Key Value Pairs, Key values should be unique

personal_detials={
    "name": "Swathi",
    "age": 30,
    "city": "Oakville",
    "employed":True
}

# Fetching values based on a key
print(personal_detials["name"])
print(personal_detials["employed"])

# Updating a key value
personal_detials["name"]="Anil Kumar Nukathoti"
print(personal_detials["name"])

# Adding a new key and value to the Dictionary

personal_detials["birth_date"]="14-05-1985"
print(personal_detials["birth_date"])

# Printing all the values based on the key
for key in personal_detials.keys():
    print(personal_detials.get(key))