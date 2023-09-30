class Parent:

    def func1(self):
        print("calling parent class method")


class child1(Parent):

    def func2(self):
        print("calling child 1 function")


class child2(Parent):

    def func3(self):
        print("calling child2 function")



obj1 = child1()
obj2 = child2()

obj1.func1()
obj1.func2()

obj2.func3()
obj2.func1()
