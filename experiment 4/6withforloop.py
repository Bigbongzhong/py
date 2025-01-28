n = int(input("enter the number:"))
sum = 0
num_digits = len(str(n))

for _ in range(num_digits):
    sum += n % 10
    n //= 10

print("Sum of digits:", sum)
