n=int(input("enter number of elements in the list:"))
list=[]
for i in range(n):
    item=int(input("enter element:"))
    list.append(item)
c=0
for i in range(0,3):
    c=list.count(i)
    print(c)