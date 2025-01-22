count = 0
for num in range(1, 101):
    if num % 5 == 0 or num % 7 == 0:
        print(num, end=" ")
        count += 1
print(f"\nTotal numbers divisible by 5 or 7: {count}")
