def abc():
    try:
        a=int(input("enter a number: "))
        b=int(input("enter a number: "))
        if a%b==0:
            print("values are completely divisible: ")
            return
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed: ")
    else:
        print("values are not completely divisible: ")
    finally:
        print("exception handeling: ")
abc()