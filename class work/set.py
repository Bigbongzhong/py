n = int(input("Enter the number of fruits: "))

s1 = set()
s2 = set()

print("Enter", n, "fruits for s1:")
for i in range(n):
    fruit = input("Enter fruit: ")
    s1.add(fruit)

print("Enter", n, "fruits for s2:")
for i in range(n):
    fruit = input("Enter fruit: ")
    s2.add(fruit)


print("\nFruits in both sets s1 and s2:", s1.intersection(s2))


print("\nFruits only in s1 but not in s2:", s1.difference(s2))

s3=s1.union(s2)
print("\nTotal unique fruits in both sets s1 and s2:", len(s3))
