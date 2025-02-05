toup=()
list=[]
n=int(input("enter number of elements:"))
for i in range(n):
    item=int(input("enter the element:"))
    list.append(item)
toup=tuple(list)
sum=0
for i in range(n):
    sum+=toup[i]
print("the average is:", sum/n)