def print_diamond_pattern(n):
    if n % 2 == 0:
        print("Please enter an odd number.")
        return
    
    mid = n // 2
    for i in range(n):
        spaces = abs(mid - i)
        stars = n - 2 * spaces
        print(" " * spaces + "*" + (" " * (stars - 2) + "*" if stars > 1 else ""))

# Example usage
for i in range(1,20):
    if(i%2!=0):
        print_diamond_pattern(i)
