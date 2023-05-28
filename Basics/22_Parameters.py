def add(a,b):
    print(a+b)

add(1,2)

def printString(str1):
    print(str1)


printString("Swathi Samyuktha Lam")
printString("Anil Kumar Nukathoti")
add(10,20)

def user_details(firstName,lastName,age,city):
    print(f"{firstName} {lastName} is of age {age} and lives in {city}")


user_details("swathi", "lam", 39, "Oakville") # Positional Arguments
user_details(firstName="Anil", lastName="Nukathoti",age=41, city="Oakville") # Keyword Argument which does not bother about the position
user_details(age=65,firstName="Sathya bala",lastName="Siripuram",city="Vijayawada")
user_details("Smaran","Nukathoti","8","Oakville")

# user_details(firstName="Smaran","Nukathoti","8","Oakville") This throws an error - always use positional argument first

user_details("Ratna",lastName="Bharath",age=40,city="Hyderabad")