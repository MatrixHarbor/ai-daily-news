class LFSR:
    def __init__(self, seed: str, tap: int):
        # Convert the seed string into a list of integers (0 or 1)
        self.seed = [int(bit) for bit in seed]
        self.tap = tap

    def step(self):
        # XOR the leftmost bit with the bit at the tap position
        leftmost_bit = self.seed.pop(0)  # Remove the leftmost bit
        new_bit = leftmost_bit ^ self.seed[-self.tap]  # XOR with the tap bit
        self.seed.append(new_bit)  # Append the new bit at the end

        # Convert the current state of the LFSR to an integer (ensure it's 8 bits)
        return int("".join(str(bit) for bit in self.seed), 2) & 0xFF

    def __str__(self):
        # Return the current state of the LFSR as a string
        return ''.join(str(bit) for bit in self.seed)

def main():
    # Create 5 LFSRs with different seeds and taps as specified
    lfsr1 = LFSR("0110100111", 2)
    lfsr2 = LFSR("0100110010", 8)
    lfsr3 = LFSR("1001011101", 5)
    lfsr4 = LFSR("0001001100", 1)
    lfsr5 = LFSR("1010011101", 7)

    # Iterate each LFSR once using the step() method and print the results
    lfsrs = [lfsr1, lfsr2, lfsr3, lfsr4, lfsr5]
    for lfsr in lfsrs:
        new_bit = lfsr.step()
        print(f"{lfsr} {new_bit}")

if __name__ == "__main__":
    main()