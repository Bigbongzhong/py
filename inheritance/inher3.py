class Grandparent:
    def __init__(self):
        print("Grandparent")

class Parent(Grandparent):
    def dummy1(self):
        print("Parent")

class Child(Parent):
    def __init__(self):
        print("Child")

c = Child()
c.dummy()
c.dummy1()
c.show()
#diff type of inheritance