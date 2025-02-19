c = 50
h = 30
d = input("Enter D values,comma-separated: ")

f = ""
i = 0
while i < len(d):
    if d[i] == ",":
        D = int(f)
        r = (2 * c * D) / h
        sq = r ** 0.5
        print(sq)
        f = ""
    else:
        f += d[i]
    i += 1


D = int(f)
result = (2 * c * D) / h
sqrt = result ** 0.5
print(sqrt)
