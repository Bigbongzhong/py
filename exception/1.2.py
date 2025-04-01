def selective_uppercase(s, n):
    if n <= 0 or n > len(s):
        return "Invalid value of n."

    s = s.lower()  # Convert entire string to lowercase
    return "".join(s[i].upper() if (i + 1) % n == 0 else s[i] for i in range(len(s)))

# Example usage
s = input("Enter a string: ")
n = int(input("Enter n: "))
print(selective_uppercase(s, n))
