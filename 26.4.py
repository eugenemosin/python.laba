from PIL import Image, ImageDraw

def letter_e():
    letter = Image.new('RGB', (200, 200))
    draw = ImageDraw.Draw(letter)
    draw.rectangle([(50, 20), (80, 180)], fill=(255, 0, 0))
    draw.rectangle([(50, 20), (160, 50)], fill=(255, 0, 0))
    draw.rectangle([(50, 85), (160, 115)], fill=(255, 0, 0))
    draw.rectangle([(50, 150), (160, 180)], fill=(255, 0, 0))
    return letter

def letter_d():
    letter = Image.new('RGB', (200, 200), color='white')
    draw = ImageDraw.Draw(letter)
    draw.rectangle([(50, 20), (80, 180)], fill=(0, 0, 255))
    draw.chord([(50, 20), (150, 180)], start=-90, end=-270, fill=(100, 150, 50), width=30)
    draw.ellipse([(85, 50), (120, 150)], fill='white')
    return letter

def draw_name():
    image = Image.new('RGB', (400, 200))
    image.paste(letter_e(), (0, 0))
    image.paste(letter_d(), (200, 0))
    image.save('name.png', 'PNG')
    image.show()


draw_name()