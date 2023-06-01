import random


def generate_random():
    for i in range(3):
        print(random.random())

generate_random()

def generate_randomInt():
    for i in range(3):
        print(random.randint(10, 100)) # print random numbers in the given range

generate_randomInt()

for i in range(10):
    print(random.randrange(10,100))

names = ["Swathi","Smaran","Anil"]
print(f"Pick a leader from the list of names {random.choice(names)}")  # Picks a name from the given list