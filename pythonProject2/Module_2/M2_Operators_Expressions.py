# 7 + 5
# 7 - 5
# 5 * 2
# 42 / 2
# 5 == 5
from math import isclose

# a = 5
# b = 2
# print(a / b) # division operator / always returns a floating-point number
# print(a % b) # 5 / 2 = 2 ...... 1
# print(a ** b)
# print(a // b)

# division operator / always returns a floating-point number
# a = 4
# b = 2
# print(a / b) # result is always a floating-point number

# floor division //
# print(10/4)
# print(10//4)
# print(6/3)
# print(6//3)

# print(abs(-7))
# print(pow(2,4))
# print(2 == 2)
# print(2 == '2')
# print(2 != 3)
# print (2 <= 2)

# number = 42                     # number
# day = "Friday"                  # string
# digits = (0,1,2,3,4,5,6,7,8,9)  # tuple
# letters = ["a","b","c"]         # list

# Above are easy


# Attention! this is important
# Comparing floating-point numbers
# x = 1.1 + 2.2
# print(x == 3.3)
# print(x)
# # give some tolerance using    isclose()   function
# from math import isclose
# x = 1.1 + 2.2
# a = isclose(x, 3.3)
# print(a)



# print(2**(6/2))
# print(2*3**4)
# print(2*3**(2*2))

# s = "Python Introduction"
# print(s[3:9])

# x = 2048 / 2
# y = x ** 0
# z = y - 1
# print(bool(z))
# print(type(z))

# s = "Johns Hopkins University"
# print(s[-24:])

# x = 40/5
# print(x)
# print(type(x))

# s = "Eagles 17 - Cowboys 0"
# print(s)
# # s = s.upper()
# # print(s)
# s = s[7:9]
# print(s)
# s = int(s)
# print(s)


e = 2.7182821828459045
x = 3**3 - (18>>1)
print(str(x) in str(e))