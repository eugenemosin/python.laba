from PIL import Image
import os


def make_preview(size, quantize_multiplier):
    image = Image.open(os.getcwd() + '//image.jpg')
    image = image.resize(size, resample=Image.BILINEAR)
    image = image.quantize(quantize_multiplier)
    image.save('res.bmp', 'BMP')
    image.show()


make_preview((400, 200), 10)

