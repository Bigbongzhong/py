def divide(a, b):
    try:
        res = a / b
        
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        return
    else:
        return res

nume = int(input("Enter the numerator: "))
denom = int(input("Enter the denominator: "))

print(divide(nume, denom))