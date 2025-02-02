# houses = ['Eric','Harvey','Selina','Justin']

# def deliver_presents_iteratively():
#     for house in houses:
#         print('deliver present to', house)
#
# deliver_presents_iteratively()

# def deliver_presents_recursively(houses):
#     if len(houses) == 1:
#         house = houses[0]
#         print("deliver presents to", house)
#
#     else:
#         mid = len(houses) // 2
#         first_half = houses[:mid]
#         second_half = houses[mid:]
#         deliver_presents_recursively(first_half)
#         deliver_presents_recursively(second_half)
#
# deliver_presents_recursively(houses)

# recursive function: base case
# def factorial_recursive(n):
#     if n == 1:
#         return 1
#     else:
#         n *= factorial_recursive(n-1)
#     print(n)
#     return n
# factorial_recursive(5)

def sum_recursive(current_number, accumulated_sum):
    if current_number == 11:
        return current_number, accumulated_sum
    else:
        return sum_recursive(current_number + 1, accumulated_sum + current_number)

# sum_recursive(1,0)
result = sum_recursive(1,0)
print(result)


# def attach_head(element, input_list):
#     return [element] + input_list
# result = attach_head(1,
#             attach_head(46,
#                         attach_head(-31,
#                                     attach_head('go',[]))))
# print(result)


# def list_sum_recursive(input_list):
#     if input_list == []:
#         return 0
#     else:
#         head = input_list[0]
#         smaller_list = input_list[1:]
#         return head + list_sum_recursive(smaller_list)
#
# result=list_sum_recursive([1,2,3])
# print(result)


# Fibonacci: Fn = Fn-1 + Fn-2
# F0 = 0
# F1 = 1
# def fibonacci_recursive(n):
#     # print("Calculating F", "(", n, ")", sep="", end=" ")
#     # print(f'Calculating F({n}),', sep="", end=" ")
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)
#
# result = fibonacci_recursive(3)
# print(result)
# n = 3
# f2+f1
# f1+f0+f1 = 2
#
# n = 5
# f4+f3
# f3+f2 + f2+f1
# f2+f1+f1+f0 + f1+f0+f1
# f1+f0+f1+f1+f0+f1+f0+f1 = 5