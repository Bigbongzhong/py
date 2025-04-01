class calculator:
    def __init__(self):
        self.result = 0

    def add(self, value, value2):
        self.result = value+value2
        return self.result

    def subtract(self, value, value2):
        self.result = value- value2
        return self.result

    def multiply(self, value, value2):
        self.result = value*value2
        return self.result

    def divide(self, value, value2):
        if value2 != 0:
            self.result = value / value2
        else:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.result
cal =calculator()
c=int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: "))
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
match (c):
    case (1):
        print(cal.add(a, b))
    case (2):
        print(cal.subtract(a, b))
    case (3):
        print(cal.multiply(a, b))
    case (4):
        print(cal.divide(a,b))