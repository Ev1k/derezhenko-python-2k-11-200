class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __str__(self):
        return f"({self.x}, {self.y})"


a = Vector(1, 3)
b = Vector(2, 4)
result = a * b
result1 = a + b
result2 = a - b
print(str(a))
print(result, result1, result2)
