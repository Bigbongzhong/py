num = int(input("Enter the number of terms: "))
a = 0
b = 1

for _ in range(num):
    print(a, end=" ")
    t = a
    a = b
    b = t + b
