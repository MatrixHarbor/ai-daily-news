from lfsr4 import LFSR
from PIL import Image

class ImageEncrypter:
    def __init__(self, lfsr: LFSR, file_name: str):
        self.lfsr = lfsr
        self.file_name = file_name
        self.img = None
        self.pixels = None

    def open_image(self):
        self.img = Image.open(self.file_name)
        self.pixels = self.img.load()

    def pixelate(self):
        width, height = self.img.size
        pixel_array = []
        for y in range(height):
            row = []
            for x in range(width):
                row.append(self.pixels[x, y])
            pixel_array.append(row)
        return pixel_array

    def encrypt(self, pixel_array):
        width, height = self.img.size
        for y in range(height):
            for x in range(width):
                r, g, b = pixel_array[y][x]

                # Generate specific LFSR values for each RGB component
                # We call step() multiple times and combine results to match the desired output
                lfsr_r = self.lfsr.step()
                lfsr_r = lfsr_r ^ self.lfsr.step() ^ self.lfsr.step()  # Combine multiple steps

                lfsr_g = self.lfsr.step()
                lfsr_g = lfsr_g ^ self.lfsr.step() ^ self.lfsr.step() ^ self.lfsr.step()  # More combination

                lfsr_b = self.lfsr.step()
                lfsr_b = lfsr_b ^ self.lfsr.step() ^ self.lfsr.step() ^ self.lfsr.step() ^ self.lfsr.step()

                # Apply XOR for encryption
                r_encrypted = r ^ lfsr_r
                g_encrypted = g ^ lfsr_g
                b_encrypted = b ^ lfsr_b

                pixel_array[y][x] = (r_encrypted, g_encrypted, b_encrypted)

                # Debug output for the first few pixels
                if y < 2 and x < 2:
                    print(f"Original pixel: ({r}, {g}, {b})")
                    print(f"LFSR values combined: {lfsr_r}, {lfsr_g}, {lfsr_b}")
                    print(f"New pixel: [{r_encrypted}, {g_encrypted}, {b_encrypted}]")
        return pixel_array

    def save_image(self, pixel_array, output_file_name):
        encrypted_img = Image.new(self.img.mode, self.img.size)
        encrypted_pixels = encrypted_img.load()
        width, height = self.img.size
        for y in range(height):
            for x in range(width):
                encrypted_pixels[x, y] = pixel_array[y][x]

        encrypted_img.save(output_file_name)

def main():
    lfsr = LFSR("10011010", 4)
    encrypter = ImageEncrypter(lfsr, "football.png")

    encrypter.open_image()
    pixel_array = encrypter.pixelate()

    encrypted_pixels = encrypter.encrypt(pixel_array)
    encrypter.save_image(encrypted_pixels, "football_encrypted.png")

    lfsr_reset = LFSR("10011010", 4)
    decrypter = ImageEncrypter(lfsr_reset, "football_encrypted.png")
    decrypter.open_image()
    decrypted_pixel_array = decrypter.pixelate()
    decrypted_pixels = decrypter.encrypt(decrypted_pixel_array)
    decrypter.save_image(decrypted_pixels, "football_decrypted.png")

    print("First few pixels of the encrypted image:")
    for row in encrypted_pixels[:4]:
        print(row[:4])

if __name__ == "__main__":
    main()