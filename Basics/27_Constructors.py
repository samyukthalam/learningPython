class Point:
    def __init__(self,x,y): # Constructor initializes an object
        self.x=x
        self.y=y
    def add(self):
        print("Add")
    def mult(self):
        print("Multi")

obj1=Point(10,20)
print(obj1.x)
print(obj1.y)
obj1.x=22
print(obj1.x)
