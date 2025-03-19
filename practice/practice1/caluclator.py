
from practice.calc import *

n1=int(input("Enter a number:"))
n2=int(input("Enter another number:"))
n3=int(input("///what do you want to do: 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division \n 5 for exponenet\n:"))
def crazy():
    match (n3):
        case (1):
            print(add(n1,n2))
        case (2):
            print(subtract(n1,n2))
        case (3):
            print(multiply(n1,n2))
        case (4):
            print(devide(n1,n2))
        case (5):
            print(expo(n1,n2))
crazy()