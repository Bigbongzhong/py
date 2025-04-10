class Parent:
    def show(self):
        print("I am Parent")

class Child(Parent):
    def display(self):
        print("I am Child")

c = Child()
c.show()
c.display()
#diff type of inheritance