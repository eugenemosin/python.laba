from PIL import Image, ImageDraw
import os
import time

def board(dimension, pixel_size):
    board_color = (255, 255, 255)
    w = dimension * pixel_size
    h = dimension * pixel_size
    image = Image.new('RGB', (w, h), board_color)
    draw = ImageDraw.Draw(image)
    for i in range(dimension):
        for j in range(dimension):
            if (i + j) % 2 == 0:
                shape = [(i * pixel_size, j * pixel_size), ((i + 1) * pixel_size, (j + 1) * pixel_size)]
                draw.rectangle(shape, fill=(0, 0, 0))
    image.save('chess.png', 'PNG')
    image.show()


board(8, 50)
