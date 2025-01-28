s = input("enter a string:")
i = 0
uppercase = ""

while i < len(s):
    uppercase += s[i].upper()
    i += 1

print(uppercase)
