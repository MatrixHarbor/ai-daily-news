# def f():
#     s = '--Inside f()'
#     print(s)
#
# f() # this is a call to f()
from numpy.f2py.crackfortran import beginpattern

# stub: define an empty function that does nothing
# def f():
#     pass
# f()

# positional arguments (required arguments)
# def f(qty,item,price): # here there are 3 positional argument
#     print(f'{qty} {item} cost {price:.2f} dollar')
# f(qty=6, item='apple', price=20.21312412)
# f(9)
# f()

# def f(my_list=[]):
#     my_list.append('xxx')
#     print(my_list)
#     return my_list
# f(my_list=[1,2,3,'hey'])

# Pass-By-Value vs Pass by reference in python
# x = 5
# x = 10
# def f(fx):
#     fx = 10
# x = 5
# f(x)

# def f(x):
#     if x < 0:
#         return
#     if x > 100:
#         return
#     print(x)
# f(2)

# def double(x):
#     x *= 2
#     return x

# x = 5
# x = double(x)
# print(x)

# def double_list(x):
#     i = 0
#     while i < len(x):
#         x[i] *= 2.0
#         i += 1
#
# a = [1,2,3,4,5]
# double_list(a)
# print(a)

# def double_list(x):
#     r = []
#     for i in x:
#         r.append(i*2)
#     return r
#
# r = [1,2,3,4,5]
# r = double_list(r) # r = double_list(r)
# print(r)

# def ave(a,b,c):
#     ave = (a+b+c) / 3
#     print(ave)
#     return ave
#
# ave(1,2,3)

def ave(a):
    total = 0
    for v in a:
        total += v
    average = total / len(a)
    print(average)
    return average

ave([1,2,3])