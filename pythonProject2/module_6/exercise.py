# factorial = 1
# def factorial_iter(n:int):
#     factorial = 1
#     for i in range(1,n):
#         factorial = factorial*i
#     return factorial
#
# print(factorial_iter(5))
#
# def factorial_rec(n:int):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial_rec(n-1)
#
# print(F_(4))

def Fi(n:int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return Fi(n-1) + Fi(n-2)
print(Fi(4))