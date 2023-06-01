class Point:  # Class is blueprint
    def addNums(self):
        print("Add nums")
    def multiNums (self):
        print("Multiply nums")

obj1 = Point() # an object is an instane of the class
obj1.addNums()
obj1.multiNums()
obj1.x=10
obj1.y=20
print(obj1.x)
print(obj1.y)

obj2=obj1
obj2.addNums()
obj2.multiNums()