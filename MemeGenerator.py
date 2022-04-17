"""Use Pillow library to generate a meme."""
from PIL import Image, ImageDraw, ImageFont


class MemeGenerator():
    """Load a file, transform image, and add text."""

    def __init__(self, output_dir):
        self.output = output_dir
        pass

    def make_meme(self, img_path, text, author, width=500) -> str:
        with open(img_path) as img:
            ratio = width/img.size[0]
            height = ratio*img.size[1]
            img = img.resize((width, height))

        if text is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.load('arial.pil')

            draw.text((10, 30), text, font=font, fill='white')
            img.save(self.output)

            return self.output
