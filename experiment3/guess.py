scnum=14
guessc=3
count=0

while count < guessc:
    num=int(input("enter the guess"))
    if num==scnum:
        print("success")
        break
    else:
        count+=1
        if count!=3:
            print("try again!!!")
        else:
            print("you lost!!")