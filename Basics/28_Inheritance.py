class Super:
    def __init__(self,className):
        self.className="Super"
    def test(self):
        print("Super Class")

class Sub(Super):  #Inheritance
    pass


class Sub2(Super):  #Inheritance
    def test2(self):
        print("Sub2")

obj1=Sub("Sub1")
obj1.test()
obj2=Sub2("Sub2")
obj2.test2()