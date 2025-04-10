class Override:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Override(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

P1 = Override(10, 20)
P2 = Override(12, 15)
P3 = P1 + P2
print("P3: ", P3)
