strand1 = ['A','T','G','C','A',"T","T","C","C","A"]
strand2 = ["C","T","-","C","G","-","A","A","-","C"]
strand3 = ["A","T","G","C","G","T","A","A","C","-"]

strands = [strand1,strand3,strand2]

total_difference1 = 0
total_difference3 = 0
differences = [total_difference1,total_difference3]

for strand in range(len(strands)-1):
    # print(strands[strand])
    # print(strand)
    for i in range(len(strand2)):
        # print(strand2[i],i)
        if strand2[i] == strands[strand][i]:
            differences[strand] += 0
            # print(differences)
# print(type(differences))
# print(type(differences[strand]))
        elif strand2[i] == "-" or strands[strand][i] == "-":
            differences[strand] += 2
        else:
            differences[strand] += 1

print(differences)
if differences[0] < differences[1]:
    print(f'strand1 is closer to strand2 with {differences[0]}')
else:
    print(f'strand3 is closer to strand2 with {differences[1]}')


# if differences[0] > differences[1]:





    # if strand2[i] == strands[i][i]:
    #     total_difference += 1
    #     print(strands[i][i])
    # elif strand2[i] == "-" or strands[i] == "-":
    #     total_difference += 2
    # else:
    #     total_difference += 1
    # print(strands[i])
    # print(strand2[i])

