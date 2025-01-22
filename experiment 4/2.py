num = int(input("Enter a number: "))
temp = num
num_str = str(num)
power = len(num_str)
sum_of_powers = 0
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** power
    temp //= 10

if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")