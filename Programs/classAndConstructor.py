class Person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print("Talk method")
obj1=Person("Swathi")
print(obj1.name)
obj1.talk()