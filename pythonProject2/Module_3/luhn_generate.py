num = input("Please enter an identifier: ")
# num = '45677'
rev_num = num[::-1] # reverse the input num so that we can compute from right to left
# print(rev_num)
sum = 0

for i in range(len(rev_num)): # for loop same thing as part 1
    if i % 2 == 0:
        a = 2 * int(rev_num[i])
        b = a // 10
        c = a % 10
        d = b + c
        e = d
    else:
        f = int(rev_num[i])
        e = f
    sum += e
# print(sum)

Checkdigit = 10 - sum % 10 # apply the algorithm mod
# print(Checkdigit)
print(f'The valid credit number is: {num}{Checkdigit} and the newly computed check digit is: {Checkdigit}')