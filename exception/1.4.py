def number_pyramid(n):
    if n <= 0 or n % 2 == 0:
        print("Please enter a positive odd number.")
        return
    
    num = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()

# Example usage
n = int(input("Enter an odd number: "))
number_pyramid(n)
