class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y)
        return result

    def __sub__(self, other):
        result = Vector(self.x - other.x, self.y - other.y)
        return result

    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y
        return result

    def __str__(self):
        return f"({self.x}, {self.y})"


a = Vector(1, 3)
b = Vector(2, 4)
result = a * b
print(result)
