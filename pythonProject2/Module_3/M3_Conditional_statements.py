# name = {'Fred':1,'Harvey':2, 'Joe':'Great'}
# print(name.get('Joe'))
# bar = 'sdagwq'
# var = 'ggg'
# if 'a' in bar:
#     print('foo')
# elif 1/0:
#     print('This will not happen')
# elif var:
#     print('this will not happen either')

# if 'f' in 'foo': print('1');print('2');print('3');print('4');print('5')


# raining = False
# print('lets go the the','beach' if not raining else 'library')
# raining = True
# print('lets go the the','beach' if not raining else 'library')
#
# age = 12
# s = 'minor' if age < 21 else 'adult'
# print(s)

# print('yes' if 'hey' in ['foo','bar'] else 'no')
# a =1
# b=2
# if a > b:
#     m = a
# else: m = b
# print(m)

# x = y = 40
# z = 1 + x if x > y else y+2
# print(z)

# for loop
# for variable in iterable:
# iterable is a collection of objects: a list or tuple
#     statements
# print()

# a = ['foo','bar','baz']
# for i in a:
#     print(i)

# a = ['foo','bar','baz']
# itr = iter(a)
# print(next(itr))
# print(next(itr))
# print(next(itr))

# itr1 = iter(a)
# itr2 = iter(a)
# print(next(itr2))
# print(next(itr2))

# print(tuple(itr))
# print(list(itr))

# for i in a:
#     print(i)


# d = {'foo':1,'bar':2,'baz':3}
# for k in d:
#     print(k)
# for k in d:
#     print(d[k])
# for k in d.keys():
#     print(k)
# for k in d.values():
#     print(k)

# i = (1,2)
# print(type(i))
# i = ['a','b',1]
# print(type(i))
# i = {'a':'hey','b':2}
# print(type(i))


# for i,j,k in [(1,2,3),(4,5,6),(7,8,9)]:
#     print(i,j,k)


# for n in (0,1,2,3,4):
#     print(n)


# x = range(5)
# print(x)
# print(type(x))
# for n in x:
#     print(n)


# print(list(x))
# print(tuple(x))

# print(list(range(5,20,3)))


# n = 5
# while n > 0:
#     n -= 1
#     print(n)


# n = 0
# while n > 0:
#     n -= 1
#     print(n)


# a = ['foo', 'bar', 'baz']
# while a:
#     print(a.pop(-1))

# n =5
# while n>0:
#     n = n-1
#     if n == 2:
#         break
#     print(n)
# print('Loop Done')

# n = 5
# while n>0:
#     n = n-1
#     print(n)
#     break
# print('Loop done')

# n = 6
# while n > 0:
#     n = n - 1
#     if n % 2 == 0:
#         continue # continue to the loop and skip print
#     print(n)
# print('Done')
#
# n = 4
# print(n % 2)

# n = 6
# while n > 0:
#     n = n - 1
#     if n == 2 or n == 3:
#         continue # continue to the loop and skip print
#     print(n)
# print('Done')

# n = 5
# while n > 0:
#     n = n - 1
#     print(n)
# else:
#     print('Loop done')

# a = ['foo', 'bar', 'baz']
# s = 'corge'
# i = 0
# while i < len(a):
#     # print(a[i])
#     # i += 1
#     if a[i] == s:
#         break
#     i = i + 1
#     print(i)
# else:
#     print('not found')

# a = ['foo','boo','boz']
# while a:
#     print(a.pop())


# while not False:
#     for i in range(5):
#         print("Hello")
#         if i ==5:
#             break
#         print("Hello")
#     print("Hello")
#     break
#     print("Hello")
# print("Hello")

# for i in range(2,6):
#     print(i)