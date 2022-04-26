"""Use Pillow library to generate a meme."""
import os
import random
from PIL import Image, ImageDraw, ImageFont


class MemeGenerator():
    """Load a file, transform image, and add quote."""

    def __init__(self, output_dir: str):
        """Create object with output path instance."""
        self.output = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Resize image and draw text."""
        with Image.open(img_path) as img:
            ratio = width/img.size[0]
            height = ratio*img.size[1]
            img = img.resize((width, height), Image.NEAREST)
            out = os.path.join(self.output, f'{random.randint(1, 1000)}.jpg')

            if text is not None and author is not None:
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype('Roboto-Regular.ttf')
                quote = f'{text} - {author}'
                draw.text((10, 30), quote, font=font, fill='black')

            img.save(out)

            return out
