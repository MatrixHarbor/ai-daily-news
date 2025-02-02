from lfsr2 import LFSR
from PIL import Image

class ImageEncrypter:
    def __init__(self, lfsr: LFSR, file_name: str):
        self.lfsr = lfsr
        self.file_name = file_name
        self.img = None
        self.pixels = None

    def open_image(self):
        # Open the image using Pillow and load the pixel data
        self.img = Image.open(self.file_name)
        self.pixels = self.img.load()

    def pixelate(self):
        # Convert the image to a 2D array of pixels
        width, height = self.img.size
        pixel_array = []
        for y in range(height):
            row = []
            for x in range(width):
                row.append(self.pixels[x, y])
            pixel_array.append(row)
        return pixel_array

    def encrypt(self, pixel_array):
        # Encrypt the pixel array using the LFSR and XOR operation
        width, height = self.img.size
        for y in range(height):
            for x in range(width):
                r, g, b = pixel_array[y][x]

                # Generate new LFSR values for each RGB component
                lfsr_r = self.lfsr.step()
                lfsr_g = self.lfsr.step()
                lfsr_b = self.lfsr.step()

                # Encrypt each component using XOR
                r_encrypted = r ^ lfsr_r
                g_encrypted = g ^ lfsr_g
                b_encrypted = b ^ lfsr_b

                # Update the pixel array with the encrypted values
                pixel_array[y][x] = (r_encrypted, g_encrypted, b_encrypted)
        return pixel_array

    def save_image(self, pixel_array, output_file_name):
        # Create a new image with the same mode and size as the original image
        encrypted_img = Image.new(self.img.mode, self.img.size)
        encrypted_pixels = encrypted_img.load()
        width, height = self.img.size
        for y in range(height):
            for x in range(width):
                encrypted_pixels[x, y] = pixel_array[y][x]

        # Save the image using the specified file name
        encrypted_img.save(output_file_name)

def main():
    # Initialize the LFSR with the specified seed and tap position
    lfsr = LFSR("10011010", 4)  # As per the assignment requirements

    # Initialize the ImageEncrypter with the LFSR and the image file name
    encrypter = ImageEncrypter(lfsr, "football.png")

    # Open the image
    encrypter.open_image()

    # Get the pixel array from the image
    pixel_array = encrypter.pixelate()

    # Encrypt the image
    encrypted_pixels = encrypter.encrypt(pixel_array)

    # Save the encrypted image
    encrypter.save_image(encrypted_pixels, "football_encrypted.png")

    # To decrypt, reinitialize the LFSR with the same seed and tap
    lfsr_reset = LFSR("10011010", 4)
    decrypter = ImageEncrypter(lfsr_reset, "football_encrypted.png")
    decrypter.open_image()
    decrypted_pixel_array = decrypter.pixelate()
    decrypted_pixels = decrypter.encrypt(decrypted_pixel_array)
    decrypter.save_image(decrypted_pixels, "football_decrypted.png")

    # Output some of the pixel values for verification
    print("First few pixels of the encrypted image:")
    for row in encrypted_pixels[:5]:
        print(row[:5])

if __name__ == "__main__":
    main()