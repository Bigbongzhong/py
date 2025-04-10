class above18:
    def __init__(self,age):
        if age>=18:
            return True
        else:
            return False
class criminalStatus:
    def __init__(self,ciminalStatus):
        if ciminalStatus==True:
            print("not eligible for voting")
        else:
            print("eligible for voting")
class below18:
    def __init__(self,age):
        if age<18:
            return True
        else:
            return False
class eligible(above18, below18):
    def __init__(self,age, status):
        self.age=age
        if above18.__init__(self,age)==True:
            criminalStatus.__init__(self, status)
        elif below18.__init__(self,age)==True:
            print("not eligible for voting")
        else:
            print("invalid age")
status=False
n=int(input("enter you age:"))
A=eligible(n, status)
#diff type of inheritance