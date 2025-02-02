from lfsr import LFSR
from PIL import Image

class ImageEncrypter:
    def __init__(self, lfsr:LFSR, file_name:str):
        self.lfsr = lfsr # initialize the ImageEncrypter with an instance
        self.file_name = file_name
        self.img = None # Placeholder
        self.pixels = None

    def open_image(self): # using PIL library
        self.img = Image.open(self.file_name)
        self.pixels = self.img.load()

    def pixelate(self): # according to https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.load
        width, height = self.img.size # get the dimensions of the image
        pixel_array = []
        for y in range(height):
            row = []
            for x in range(width):
                row.append(self.pixels[x, y])
            pixel_array.append(row)
        return pixel_array # return the complete 2D array of pixels

    def encrypt(self, pixel_array): # use lfsr and XOR operator
        width, height = self.img.size
        for y in range(height):
            for x in range(width):
                r,g,b = pixel_array[y][x]
                lfsr_r = self.lfsr.step()
                lfsr_g = self.lfsr.step()
                lfsr_b = self.lfsr.step()
# here I asked Liv and my friend. They suggested me to generate a full 8-bit binary number
                lfsr_r = int(''.join(str(self.lfsr.step())for _ in range(8)), 2)
                lfsr_g = int(''.join(str(self.lfsr.step())for _ in range(8)), 2)
                lfsr_b = int(''.join(str(self.lfsr.step())for _ in range(8)), 2)
                r_encrypted = r^lfsr_r
                g_encrypted = g^lfsr_g
                b_encrypted = b^lfsr_b
                pixel_array[y][x] = (r_encrypted, g_encrypted, b_encrypted)
        return pixel_array

    def save_image(self,pixel_array,output_file_name): # https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save
        encrypted_img = Image.new(self.img.mode, self.img.size)
        encrypted_pixels = encrypted_img.load()
        width, height = self.img.size
        for y in range(height):
            for x in range(width):
                encrypted_pixels[x, y] = pixel_array[y][x]
        encrypted_img.save(output_file_name)

def main():
    lfsr = LFSR("10011010",5)
    encrypter = ImageEncrypter(lfsr, "football.png")
    encrypter.open_image() # open
    pixel_array = encrypter.pixelate() # get the pixel array

    # encrypt the image
    encrypted_pixels = encrypter.encrypt(pixel_array)
    encrypter.save_image(encrypted_pixels,"football_encrypted.png")

    lfsr_reset = LFSR("10011010",5)
    decrypter = ImageEncrypter(lfsr_reset, "football_encrypted.png")
    decrypter.open_image()
    decrypted_pixel_array = decrypter.pixelate()
    decrypted_pixels = decrypter.encrypt(decrypted_pixel_array)
    decrypter.save_image(decrypted_pixels,"football_decrypted.png")

    # for row in encrypted_pixels[:4]:
    #     print(row[:4])

if __name__ == "__main__":
    main()