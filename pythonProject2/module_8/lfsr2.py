class LFSR:
    def __init__(self, seed: str, tap: int):
        self.seed = [int(bit) for bit in seed]  # Convert seed string to a list of integers
        self.tap = tap

    def step(self):
        # XOR the leftmost bit with the tap bit
        leftmost_bit = self.seed.pop(0)
        new_bit = leftmost_bit ^ self.seed[-self.tap]
        self.seed.append(new_bit)  # Append the new bit at the end

        # Convert the current state of the seed to an 8-bit integer
        return int("".join(str(bit) for bit in self.seed), 2) & 0xFF  # Mask to ensure 8 bits

    def __str__(self):
        return ''.join(str(bit) for bit in self.seed)

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