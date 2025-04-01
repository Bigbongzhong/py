while True:
    i=0
    b=[]
    while i<5:
            
        try:
            a=int(input("enter a number: "))
            b.append(a)
            i=i+1
        except ValueError:
            
            print("Error: Please enter a valid number")
        
    try:
        c=int(input("enter the index: "))
        print(b[c])
        break
    except IndexError:
        print("Error: Index out of range")