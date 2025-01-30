li=[]
for j in range(20,1000):
    num_digits = len(str(j))
    sum = 0
    n=j
    for digit in str(j):
        sum += int(digit) ** num_digits
    # print(sum)
    if sum == n:
        # print(n, "is an Armstrong number")
        li.append(j)
    # else:
    #     print(n, "is not an Armstrong number")
print(li)
