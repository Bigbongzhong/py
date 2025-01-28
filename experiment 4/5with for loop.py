n = int(input("enter a number:"))
original = n
reverse = 0
nu = len(str(n))

for _ in range(nu):
    d = n % 10
    reverse = reverse * 10 + d
    n //= 10

if original == reverse:
    print(original, "is a palindrome number")
else:
    print(original, "is not a palindrome number")
