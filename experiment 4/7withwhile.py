i = 1
j = 100
count = 0

while i <= j:
    if i % 5 == 0 or i % 7 == 0:
        count += 1
        print(i)
    i += 1

print("Total numbers divisible by 5 or 7:", count)
