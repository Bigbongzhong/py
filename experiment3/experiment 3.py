#divisible by 3 and 5
x=int(input("Enter a number: "))
if (x%3==0 and x%5==0):
    print("Number is divisible by both")
if (x%3==0 and x%5!=0):
    print("Number is only divisible by 3:")
if (x%5==0 and x%3!=0):
    print("Number is only divisible by 5")
else:
    print("its not divisible by any of them")
#output
'''Enter a number: 56
its not divisible by any of them'''



#number Multiple 5
y=int(input("Enter the number: "))
if y%5==0:
    print("Number is multiple of 5")

else:
    print("Number is not multiple of 5")
#output
'''Enter the number: 5000
Number is multiple of 5'''






#Greatest number!
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if(a>b):
    print(a ,"is greater than", b)
elif(b>a):
    print(b ,"is greater than", a)
elif(b==a):
    print("Both are equal")
    #output
    '''Enter first number: 2
Enter second number: 5
5 is greater than 2'''



#greatest among three numbers
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter the 3rd number: "))
if a>b:
    if a>c:
        print(a, " Is the Greeatest!")
    elif c>a:
        print(c," is greatest of all!")
elif b>a:
    if b>c:
        print(b ," is the greatest!")
    elif c>b:
        print(c," is the greatest")
#output
'''Enter 1st number: 5
Enter 2nd number: 6
Enter the 3rd number: 7
7  is the greatest'''




#real or distinct roots
a=float(input("enter the value of a: "))
b=float(input("enter the value of b: "))
c=float(input("enter the value of c: "))
d=((b**2)-(4*a*c))
if(d>0):
    print("real and distinct roots")
elif(d<0):
    print("imaginary roots")
else:
    print("the roots are real and same")
r1=((-b)+(d**0.5))/2*a
r2=((-b)-(d**0.5))/2*a
print("the roots are",r1,r2)
#output
'''enter the value of a: 4
enter the value of b: 5
enter the value of c: 6
imaginary roots
the roots are (-9.999999999999998+16.852299546352718j) (-10.000000000000002-16.852299546352718j)'''



#check weather year is leap year or not
a=int(input("enter the year: "))
if a%4==0:
    print("year is a leap year")
else:
    print("year is not a leap year")
#output
'''enter the year: 2004
year is a leap year'''





#find the next date
days=[31,28,31,30,31,30,31,31,30,31,30,31]
d=int(input("Enter day:"))
m=int(input("Enter month:"))
y=int(input("Enter year:"))
if y%4==0:
    days[1]+=1
    if m<12:
        if d<days[m-1]:
            d+=1
        elif d==days[m-1]:
            m+=1
    elif m==12:
        if d<days[m-1]:
            d+=1
        elif d==days[m-1]:
            m=1
            d=1
            y+=1
else:
    if m<12:
        if d<days[m-1]:
            d+=1
        elif d==days[m-1]:
            m+=1
    elif m==12:
        if d<days[m-1]:
            d+=1
        elif d==days[m-1]:
            m=1
            d=1
            y+=1
print("next date is", d,m,y)
#output
'''Enter day:31
Enter month:12
Enter year:2004
next date is 1 1 2005'''



#calculate cgpa

name=input("enter the name:")
roll=input("enter the roll:")
sem=input("enter the semester:")
sap=input("enter sap:")
course=input("enter course:")

PDS=float(input("enter the name:"))
Python=float(input("enter the name:"))
Chemistry=float(input("enter the name:"))
English=float(input("enter the name:"))
Physics=float(input("enter the name:"))
per=((PDS+Python+Chemistry+English+Physics)/500)*100
cgpa=per/10
grade="f"
if cgpa>0 and cgpa<=3.4:
    grade = "f"
if cgpa>3.4 and cgpa<=5:
    grade ="c+"
if cgpa>5 and cgpa<=6:
    grade ="b"
if cgpa>6 and cgpa<=7:
    grade="b+"
if cgpa>7 and cgpa<=8:
    grade="a"
if cgpa>8 and cgpa<=9:
    grade ="a+"
if cgpa>9 and cgpa<=10:
    grade ="o"
print(name)
print(roll,"\t", sap)
print(sem, "\t", course)
print("subject marks:")
print(PDS,"\n",Physics,"\n",Chemistry,"\n",Python,"\n",English,"\n",per,"\n",cgpa,"\n",grade,"\n")
#output
'''Enter day:31
Enter month:12
Enter year:2004
next date is 31 1 2005
PS D:\py> python -u "d:\py\experiment3\edf.py"
Enter day:31
Enter month:12
Enter year:2004
next date is 31 1 2005
PS D:\py> python -u "d:\py\experiment3\edf.py"
Enter day:31
Enter month:12
Enter year:2004
next date is 31 1 2005
PS D:\py> python -u "d:\py\experiment3\edf.py"
Enter day:31
Enter month:12
Enter year:2004
next date is 1 1 2005
PS D:\py> python -u "d:\py\experiment3\edf.py"
Enter day:28
Enter month:2
Enter year:2024
next date is 29 2 2024
PS D:\py> python -u "d:\py\experiment3\edf.py"
enter the name:surya
enter the roll:5900
enter the semester:1
enter sap:599
enter course:btech
enter the name:surya
Traceback (most recent call last):
  File "d:\py\experiment3\edf.py", line 7, in <module>
    PDS=float(input("enter the name:"))
ValueError: could not convert string to float: 'surya'
PS D:\py> python -u "d:\py\experiment3\edf.py"
enter the name:su
enter the roll:833
enter the semester:1
enter sap:435
enter course:btech
enter pds marks:78
enter python marks:20
enter chem marks:67
enter english marks:87
enter physics marks:99
su
833      435
1        btech
subject marks:
78.0
 99.0
 67.0
 20.0
 87.0
 70.19999999999999
 7.019999999999999
 a'''