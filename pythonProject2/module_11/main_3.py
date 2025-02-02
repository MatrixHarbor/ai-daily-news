import numpy as np
from hillcipher import HillCipher

def main():
    cipher = HillCipher()

    plaintext = "ATTACKATDAWN"
    keys = [
        np.array([[19, 8, 4], [3, 12, 7]]),
        np.array([[7, 8], [11, 11]]),
        np.array([[5, 15], [4, 12]])
    ]

    for key in keys:
        if key.shape[0] != key.shape[1]:
            print("\nThe matrix is not square.\n")
            continue

        det = cipher.determinant(key)
        if det == 0:
            print("The determinant = 0\n")
            continue

        print("The matrix is invertible.\n")

        # Encode plaintext
        encoded_plaintext = cipher.encode(plaintext)
        print(f"Plaintext: {plaintext}")

        # Correctly formatted plaintext column vectors
        print("Plaintext column vectors: [", end="")
        print(", ".join(
            f"array({np.array(encoded_plaintext[i:i + 2]).reshape(2, 1).tolist()})" for i in range(0, len(encoded_plaintext), 2)),
              end="")
        print("]")

        # Encrypt plaintext
        ciphertext = cipher.encrypt(encoded_plaintext, key)

        # Correctly formatted ciphertext column vectors
        encoded_ciphertext = cipher.decode(ciphertext)
        print(f"\nCiphertext: {encoded_ciphertext}")
        print("Ciphertext column vectors: [", end="")
        print(", ".join(f"array({np.array(ciphertext[i:i + 2]).reshape(2, 1).tolist()})" for i in range(0, len(ciphertext), 2)), end="")
        print("]")

        # Decrypt ciphertext
        decryption_key = cipher.get_decryption_key(key)
        decrypted_numeric = cipher.decrypt(ciphertext, decryption_key)
        decrypted_text = cipher.decode(decrypted_numeric)
        print(f"\nPlaintext: {decrypted_text}")

        # Display plaintext column vectors again
        print("Plaintext column vectors: [", end="")
        print(", ".join(
            f"array({np.array(decrypted_numeric[i:i + 2]).reshape(2, 1).tolist()})" for i in range(0, len(decrypted_numeric), 2)),
              end="")
        print("]\n")


if __name__ == "__main__":
    main()