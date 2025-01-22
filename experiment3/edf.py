x=int(input("Enter a number: "))
if (x%3==0 and x%5==0):
    print("Number is divisible by both")
if (x%3==0 and x%5!=0):
    print("Number is only divisible by 3:")
if (x%5==0 and x%3!=0):
    print("Number is only divisible by 5")
else:
    print("its not divisible by any of them")