# Numeric types
# str data type: represent textual data
# bytes & bytearray
# Boolean values with the bool data type
import sys

# built-in data types
# Class                 Basic Type
# int                   Integer numbers
# float                 Floating-point numbers
# complex               Complex num
# str                   Strings and characters
# bytes, bytearray      Bytes
# bool                  Boolean values

# more readable :  1_000_000 means a million

# generally python is decimal
# 0b10 : Binary         base 2
# 0o10 : Octal          base 8
# 0x10 : Hexadecimal    base 16

# .as_integer_ratio()
# .bit_count()
# .bit_length()
# .from_bytes
# .to_bytes()
# .is_integer()

# print((42).as_integer_ratio())
# signal = 0b11010110
# set_bits = signal.bit_count()
# if set_bits % 2 == 0:
#     print("Even parity")
# else:
#     print("Odd parity")

# int(42.0)  output:  42

# Floating-Point Numbers: 1.0   3.1415   -2.42
# print(type(-.2))
# print(4e1)
# print(.4e1)
# print(7E-2)
# print(.7E-2)
# print(2e-323)
# print(1e-324)

# G = (800).as_integer_ratio()
# print(G)

# A = (1.1).hex()
# print(A)

# B = (42.0).is_integer()
# print(B)
# print(type(B))
# print(type(42.0))
# C = (42.1).is_integer()
# print(C)
# print(type(C))
# print(type(42.1))


# Complex Numbers
# print(type(2+3j))
# print(2+3j)

# number = 2+3j
# print(number)
# C = number.conjugate()
# print(C)

# print(complex())
# print(complex(1))
# print(complex(1,1))
# print(complex(0,7))
# print(complex(1,-7))


# Strings and Characters
# print(type("hey"))
# print("I am a string")

# print("")
# print(len(""))

# import numpy as np
# import pandas as pd

# print("a\nb")
# print("\141") # Octal
# print("\x61") # Hex

# Escape Sequences in Strings
# print("Before\\After")
# print("Before\tAfter")
# print("Before After")
# print(r"Before\tAfter") # Raw string

# F-string Literals: formatted strings or f-strings
# name = "Jane"
# print(f"I don't know who is {name}, so can you tell me")
# income = 1234.1294
# print(f"{name}'s income is 💲{income}")
# print(f"{name}'s income is 💲{income:.2f}")


# String Methods
# String_Method = "paris is so beautiful".capitalize()
# print(String_Method)
# a = "".join(["I"," love"," you"])
# print(a)
# b = "===I really===".strip("=")
# print(b)
# c = "---really really---".removeprefix("---")
# print(c)
# d = "+++love you+++".removesuffix("++")
# print(d)
# e = "kiss me".title()
# print(e)
# f = "kiss me".upper()
# print(f)


# filename = "paris.main.py"
# if filename.endswith(".py"):
#     print(f"It is a python file: {filename}.")
# a = "123abc".isalnum() # True if all are alphanumeric
# b = "123abc".isalpha()
# c = "123".isdigit()
# d = "123abc".islower()
# e = "A123".istitle()
# f = "123abc".isupper()
# g = "123ABC".isupper()
# print(a,b,c,d,e,f,g)
# # print(type(a),type(b),type(c),type(d),type(e),type(f))



# sentence = "Never gonna give you up"
# words = sentence.split()
# print(words)
# print(words[0])
# print(words[1])
# print(words[2])
# print(words[-1])
# print(words[-2])
# print(f"{words[0]} {words[1]} {words[2]}")
# numbers = "1-2-3-4-5"
# head, sep, tail = numbers.partition("-")
# print(head)
# print(sep)
# print(tail)



# def cipher(text):
#     alphabet = "abcdefg"
#     shifted = "defghij"
#     table = str.maketrans(alphabet, shifted)
#     return text. translate(table)
# print(cipher("abcd"))
# print(len(cipher("abcd")))


# a = "Pythonista"
# print(a[0])
# print(a[8])
# print(a[:6])
# print(a[:6].upper())
# print(a[:6].lower())


# str()
# a = "".join([1, 2, 3]) # this doesn't work
# b = " ".join(str(value) for value in [1, 2, 3])
# print(b)


# .__str__()
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"My name is {self.name}, and I'm {self.age} years old."
# harvey = Person("Harvey", 22)
# print(str(harvey))
# OR
# from person import Person  # means from person.py file, you import Person function, so you need another file named person.py
# harvey = Person("Harvey", 22)
# print(str(harvey))


# Bytes and Bytearrays
# a = type(b"This is a bytes literal")
# print(a)

# bytes("Hello World!",encoding="utf-8")
# print(bytes("Hello World!",encoding="utf-8"))

# print(bytes([65,66,67,]))       # immutable
# print(bytearray([65,66,67,]))   # mutable

# print(type(False))

# print(issubclass(bool,int))
# print(issubclass(bool,str))
#
# print(True+True)


# Built-in bool() Function
# print(bool(0))
# print(bool(1))
# print(bool(2.1))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point1 = Point(0, 0)
print(point1.x, point1.y)
print(bool(point1))

