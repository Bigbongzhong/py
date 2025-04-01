def divide(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed."
    else:
        return res
try:
    nume = int(input("Enter the numerator: "))
    denom = int(input("Enter the denominator: "))
    print(divide(nume, denom))
except ValueError:
    print("Please enter a valid number.")