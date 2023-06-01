try:
    age = int(input("Enter Age >> "))
    print(age)
    income=1000
    factor=income/age
except ValueError:
    print("Invalid Value")
except ZeroDivisionError:
    print("Age cannot be 0")
