# from clas2 import Charge
#
# if __name__ == "__main__":
#     c = Charge(1.0,2.0,2)
#
#     # print(c)
#     # print(c.q)
#     print(c.coulomb_to_electrons(c.q))

from PIL import Image
# print(Image.__name__ + "was imported successfully")

class LFSR:
    def __init__(self, seed:str, tap:int):
        # for bit in seed: # convert seed string to a list
        #     self.seed = [int(bit)]
        self.seed = [int(bit) for bit in seed]
        self.tap = tap

    def bit(self, i:int):
        return self.seed[i]

    def step(self): # using lfsr algorithm
        leftmost_bit = self.seed.pop(0) # remove index 0
        new_bit = leftmost_bit ^ self.seed[-self.tap] # use ^ method at the tap position
        self.seed.append(new_bit) # append new bit to the rightmost
        return new_bit

    def __str__(self):
        return ''.join(str(bit) for bit in self.seed)
        # for bit in self.seed:
        #     return ''.join(str(bit)) # back to string

def main():
    lfsr1 = LFSR("0110100111",2)
    lfsr2 = LFSR("0100110010",8)
    lfsr3 = LFSR("1001011101",5)
    lfsr4 = LFSR("0001001100",1)
    lfsr5 = LFSR("1010011101",7)

    lfsrs = [lfsr1,lfsr2,lfsr3,lfsr4,lfsr5]

    for lfsr in lfsrs:
        new_bit = lfsr.step()
        print(f"{lfsr} {new_bit}")

if __name__ == "__main__":
    main()