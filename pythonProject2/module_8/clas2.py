# class Charge:
#     coulumb = 6.24E18
#
#     def __int__(self, x=0, y=0, q=1):
#         self.x = x
#         self.y = y
#         self.q = self.coulumb_to_electrons(q)
#
#     def coulumb_to_electrons(self,C):
#         return C * self.coulumb
#
#     def __str__(self):
#         return f"{self.x} {self.y} {self.q}"
#
# c1 = Charge(1,2)
# c2 = Charge()
# print(c1)
# print(c2)

class Charge:
    coulomb = 6.24E18  # 注意这里是 "coulomb" 不是 "coulumb"

    def __init__(self, x=0.0, y=0.0, q=1):
        self.x = x # constructor
        self.y = y # constructor
        self.q = self.coulomb_to_electrons(q) # constructor

    def coulomb_to_electrons(self, C):
        return C * self.coulomb

    def __str__(self):
        return f"{self.x} {self.y} {self.q}"

c1 = Charge(3.5, 6.5) # constructor is called automatically
c2 = Charge()               # constructor is called automatically
print(c1)
print(c2)