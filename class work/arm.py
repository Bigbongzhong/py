
list=[i for i in range(1000) if i==sum(int(dig) ** len(str(i)) for dig in str(i))]
print(list)