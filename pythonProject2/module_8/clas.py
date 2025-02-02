# class Charge:
#     coulumb = 6.24E18
#
#     def __int__(self, x=0.0, y=0.0, q=1):
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
# print(Charge.__name__)
# print(Charge.coulumb)
# print(Charge.__module__)
# print(Charge.__doc__)
# print(Charge.coulumb_to_electrons)
# print(Charge.__bases__)
# print(Charge.__dict__)

# class Charge:
#     coulumb = 6.24E18
#
#     def __init__(self, q):
#         self.q = self.coulumb_to_electrons(q)
#
#     def coulumb_to_electrons(self, C):
#         return C * self.coulumb
#
# c1 = Charge(3)
# c2 = Charge(1.5)
#
# print(id(c1))
# print(id(c2))
#
# print(c1.q)
# print(c2.q)
# print(c1.coulumb_to_electrons(1))
# print(c2.coulumb_to_electrons(0.5))
# print(Charge(3).coulumb_to_electrons(1))


# class Charge:
#     coulomb = 6.24E18
#
#     def __init__(self, q):
#         self.q = q
#
#     def coulomb_to_electrons(self, C):
#         return C * self.q
#
# c1 = Charge(3)
# c2 = Charge(1.5)
# print(c1.q)
# print(c2.q)
# print(c1.coulomb_to_electrons(2))
# print(c2.coulomb_to_electrons(2))


class Charge:
    coulumb = 6.24E18

    def __init__(self, x=0.0, y=0.0, q=1):
        self.x = x
        self.y = y
        self.q = self.coulumb_to_electrons(q)

    def coulumb_to_electrons(self,C):
        return C * self.coulumb

    def __str__(self):
        return f"{self.x} {self.y} {self.q}"

c1 = Charge(3.5, 6.5)
c2 = Charge()
print(c1)
print(c2)