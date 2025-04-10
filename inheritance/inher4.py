class parent:
    def print(self):
        print("Inside parent class")

class child(parent):
    def print(self):
        print("Inside child class")

C = child()
C.print()