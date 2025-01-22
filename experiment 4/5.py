num = int(input("Enter a number: "))
temp = num
reverse = 0
while temp > 0:
    reverse = reverse * 10 + temp % 10
    temp //= 10

if reverse == num:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
