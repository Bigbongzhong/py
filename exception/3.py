def count(a, b):
    if a<100 or b>150:
        raise ValueError("check the range of input")
    
    for i in range (a, b+1):
        print(i)
    return

c=int(input("enter a number: "))
d=int(input("enter a number: "))
count(c, d)
