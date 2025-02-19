c = 50
h = 30
d = [int(d) for d in input("Enter comma-separated values for D: ").split(",")]
for i in d:
    print(((2*c*i)/h)**0.5)
