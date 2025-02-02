class Number:
    def __init__(self, n):
        self.n = n

    def add(self,n1,n2=4):
        return self.n + n2
n1 = Number(36)
n2 = Number(4)

print(n1.add(n2))