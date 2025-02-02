import numpy as np

class HillCipher:
    def determinant(self, key_matrix):
        return int(np.round(np.linalg.det(key_matrix)))

    def invertible(self, key_matrix):
        if key_matrix.shape[0] != key_matrix.shape[1]:
            print("The matrix is not square.")
            return False

        det = self.determinant(key_matrix)
        if det == 0:
            print("The determinant is 0.")
            return False

        print("The matrix is invertible.")
        return True

    def mod_inverse(self, determinant, modulus):
        for i in range(1, modulus):
            if (determinant * i) % modulus == 1:
                return i
        raise ValueError("No modular inverse found.")

    def encode(self, str_):
        return [ord(char.upper()) - ord('A') for char in str_ if char.isalpha()]

    def decode(self, str_):
        return ''.join(chr(num + ord('A')) for num in str_)

    def encrypt(self, plaintext, key):
        # Split plaintext into 2-character chunks
        chunks = [plaintext[i:i + 2] for i in range(0, len(plaintext), 2)]

        # Ensure each chunk is size 2 by padding with 'X' (23) if needed
        if len(chunks[-1]) < 2:
            chunks[-1].append(23)  # Numeric for 'X'

        ciphertext = []

        for chunk in chunks:
            # Convert chunk to 2x1 column vector
            vector = np.array(chunk).reshape(2, 1)
            encrypted_vector = (np.dot(key, vector) % 26).flatten() # Encrypt: Multiply key matrix by vector, mod 26
            ciphertext.extend(encrypted_vector) # Append encrypted values to ciphertext
        return ciphertext

    def decrypt(self, ciphertext, key):
        # Split ciphertext into 2-character chunks
        chunks = [ciphertext[i:i + 2] for i in range(0, len(ciphertext), 2)]

        plaintext = []

        for chunk in chunks:
            # Convert chunk to 2x1 column vector
            vector = np.array(chunk).reshape(2, 1)
            decrypted_vector = (np.dot(key, vector) % 26).flatten() # Decrypt: Multiply decryption key matrix by vector, mod 26
            plaintext.extend(decrypted_vector) # Append decrypted values to plaintext
        return plaintext

    def get_decryption_key(self, key):
        det = self.determinant(key)
        mod_inv = self.mod_inverse(det, 26)
        # Compute adjugate (transpose of cofactors) and multiply by modular inverse
        adjugate = np.array([[key[1, 1], -key[0, 1]],
                             [-key[1, 0], key[0, 0]]])
        decryption_key = (mod_inv * adjugate) % 26
        return decryption_key.astype(int)