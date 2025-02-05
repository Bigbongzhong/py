#list compression
a="hello world"
list=[i for i in a]
# print(list)

#even no's
list2=[i for i in range(200) if i%2==0]
# print(list2)

#exponent of power 2
list3=[i**2 for i in range(100)]
# print(list3)

#divisibility check
list4=[i for i in range(200) if i%3==0 or i%5==0 or i%7==0]
# print(list4)

#only numbers
b="one 1 two 2"
list5=[i for i in b if i.isnumeric()]
print(list5)
list6=[i for i in b if i.isalpha()]
print(list6)