class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def slope_to(self, other):
        if self.x == other.x:
            return float('inf')
        return (other.y - self.y) / (other.x - self.x)

    def __repr__(self):
        return f"({self.x}, {self.y})"