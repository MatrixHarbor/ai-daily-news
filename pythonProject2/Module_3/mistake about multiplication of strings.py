num = '3967'
sum = 0
for i in range(len(num)): # range means from 0 to a number-1. and len means the number is the length of num which is 5
    if i % 2 == 0:
        b = 2 * num[i]
        print(num[i])
        print(b)
        print(type(b))
        c = int(b) // 10
        # print(c)
        d = int(b) % 10
        e = c + d
        f = int(e)
        # print(f)
    # else:
    #     a = num[i]
    #     f = int(a)
#     sum += f
# print(sum)
