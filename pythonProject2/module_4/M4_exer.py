strand1 = ['A','T','G','C','A',"T","T","C","C","A"]
strand2 = ["C","T","-","C","G","-","A","A","-","C"]
strand3 = ["A","T","G","C","G","T","A","A","C","-"]
total_difference1 = 0
total_difference3 = 0

for i in range(len(strand2)):
    if strand2[i] == strand1[i]:
        total_difference1 += 0
    elif strand2[i] == "-" or strand1[i] == "-":
        total_difference1 += 2
    else:
        total_difference1 += 1
print(total_difference1)
# print(strand2[i])
# print(strand1[i])
for i in range(len(strand3)):
    if strand2[i] == strand3[i]:
        total_difference3 += 0
    elif strand2[i] == "-" or strand3[i] == "-":
        total_difference3 += 2
    else:
        total_difference3 += 1
print(total_difference3)

if total_difference1 > total_difference3:
    print(f'strand3 is closer to strand2 and the difference is {total_difference3}')
else:
    print(f'strand1 is closer to strand2 and the difference is {total_difference1}')
