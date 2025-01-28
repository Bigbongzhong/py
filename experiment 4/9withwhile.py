n = int(input("enter a number:"))
i = 2
prime = True

while i <= n // 2:
    if n % i == 0:
        prime = False
        break
    i += 1

if prime and n > 1:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
