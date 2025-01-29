l1=[]
for num in range(1,1001):
    t = num
    num1 = str(num)
    power = len(num1)
    sum_of_powers = 0
    while t > 0:
        digit = t% 10
        sum_of_powers += digit ** power
        t //= 10
    if sum_of_powers == num:
        # print(num , end=" ")
        l1.append(num)
print(l1)