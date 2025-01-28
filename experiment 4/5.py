num = int(input("Enter a number: "))
temp = num
r = 0
while temp > 0:
    r = r * 10 + temp % 10
    temp = temp//10

if r == num:
    print(num,"is a palindrome.")
else:
    print(num,"is not a palindrome.")
