#ques 1 and 2

class student():
    def __init__(self, name, sapId, marks):
        self.name = name
        self.sapId = sapId
        self.marks = marks
    def display(self):
        print("Name:", self.name)
        print("apId:", self.sapId)
        print("marks:", self.marks)
        
    def markPercentage(self):
        total=sum(self.marks)
        markAvg=total/(100*len(self.marks))
        return markAvg*100
    def displayResult(self):
        if all(i>40 for i in self.marks):
            print(self.name, "pass")
        else:
            print(self.name, "fail")

Students = []

a=int(input("enter number of students: "))
for i in range(a):
    name = input("enter name: ")
    sapId = input("enter sapId: ")
    marks = []
    for j in range(3):
        marks.append(int(input("enter marks: ")))
    Students.append(student(name, sapId, marks))
def averageOfClass(Students):
    sun=0
    for i in Students:
        sun+=i.markPercentage()
    return(sun/len(Students))
for i in Students:
    i.display()
    i.displayResult()
print("class average percentage: ", averageOfClass(Students))

#ques 3
class above18:
    def __init__(self,age):
        if age>=18:
            return True
        else:
            return False
class criminalStatus:
    def __init__(self,ciminalStatus):
        if ciminalStatus==True:
            print("not eligible for voting")
        else:
            print("eligible for voting")
class below18:
    def __init__(self,age):
        if age<18:
            return True
        else:
            return False
class eligible(above18, below18):
    def __init__(self,age, status):
        self.age=age
        if above18.__init__(self,age)==True:
            criminalStatus.__init__(self, status)
        elif below18.__init__(self,age)==True:
            print("not eligible for voting")
        else:
            print("invalid age")
status=False
n=int(input("enter you age:"))
A=eligible(n, status)

class Parent:
    def show(self):
        print("I am Parent")

class Child(Parent):
    def display(self):
        print("I am Child")

c = Child()
c.show()
c.display()

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

#ques 4
class parent:
    def print(self):
        print("Inside parent class")

class child(parent):
    def print(self):
        print("Inside child class")

C = child()
C.print()

#ques 5
class Override:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Override(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

P1 = Override(10, 20)
P2 = Override(12, 15)
P3 = P1 + P2
print("P3: ", P3)
