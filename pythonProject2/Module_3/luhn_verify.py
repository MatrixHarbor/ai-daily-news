num = input("Please enter a credit card number: ")
# num = '3379513561108795'
sum = 0 # define a new variable to compute the checksum
for i in range(len(num)): # for loop to go through every number in num # range means from 0 to a number-1. and len means the number is the length of num which is 5
    if i % 2 == 1: # since python start from 0, this is for the even number
        a = int(num[i]) # even number does not change
        # print(a)
        e = 0
        f = a # this is the outcome of the even number in num
    else: # for the odd number using mod 3mod10 = 3 get the ones digit & quotient 32 // 10 = 3 get the tens digit
        b = 2*int(num[i])
        # print(b)
        c = b % 10 # get the ones digit
        # print(c)
        d = b // 10 # get the tens digit
        # print(d)
        e = int(c) + int(d) # the sum of two digits
        f = e # this is the outcome of the odd number in num
    # print(f)
    sum += f # add all the outcomes from odd and even number
# print(sum)
if sum % 10 == 0:
    print(f'Checksum = {sum%10}')
    print(num + ' is a valid CC number.' )
else:
    print(f'Checksum = {sum%10}')
    print(num + ' is an invalid CC number.')







num = input("Please enter a credit card number: ")
# num = '3379513561108795'
sum = 0 # define a new variable to compute the checksum
for i in range(len(num)): # for loop to go through every number in num
    if i % 2 == 1: # since python start from 0, this is for the even number
        a = int(num[i]) # even number does not change
        # print(a)
        e = 0
        f = a # this is the outcome of the even number in num
    else: # for the odd number using mod 3mod10 = 3 get the ones digit & quotient 32 // 10 = 3 get the tens digit
        b = 2*int(num[i])
        # print(b)
        c = b % 10 # get the ones digit
        # print(c)
        d = b // 10 # get the tens digit
        # print(d)
        e = int(c) + int(d) # the sum of two digits
        f = e # this is the outcome of the odd number in num
    # print(f)
    sum += f # add all the outcomes from odd and even number
# print(sum)
if sum % 10 == 0:
    print(f'Checksum = {sum%10}')
    print(num + ' is a valid CC number.' )
else:
    print(f'Checksum = {sum%10}')
    print(num + ' is an invalid CC number.')