"""
It is used for create meme.
"""
import os
from random import randint
from PIL import Image, ImageDraw, ImageFont
import textwrap
import random


class MemeEngine:
    """
    The class is used for creating meme and it takes 1 attribute.
Attribute:
    output_dir: str -> where the file will be created.
    """
    counter = randint(0, 10000)

    def __init__(self, output_dir: str):
        self.path = output_dir
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        self.id = MemeEngine.counter
        MemeEngine.counter += 1

    def make_meme(self, img_path, text, author, width=500):
        """
        To create meme with img_path, text (quote),
        author and width (default is 500).
        """
        if width >= 500:
            width = 500
            with Image.open(img_path) as image:
                c_width, c_height = image.size
                ratio = width / c_width
                height = int(ratio * c_height)
                image = image.resize((width, height))
                draw = ImageDraw.Draw(image)
                font = ImageFont.truetype('./LilitaOne-Regular.ttf', size=35)
                text = textwrap.fill(text=text, width=26)
                text = f'-{text} \n -{author}'
                x = random.randint(20, 50)
                y = random.randint(20, 300)
                draw.text((x, y), text, font=font, fill='white')
                random_number = randint(0, 1000000) * self.id
                path = os.path.join(self.path, f'{random_number}.png')
                image.save(path)
                return path
