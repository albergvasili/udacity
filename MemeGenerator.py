"""Use Pillow library to generate a meme."""
from PIL import Image, ImageDraw, ImageFont


class MemeGenerator():
    """Load a file, transform image, and add quote."""

    def __init__(self, output_dir: str):
        """Create object with output path instance."""
        self.output = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Resize image and draw text."""
        with open(img_path) as img:
            ratio = width/img.size[0]
            height = ratio*img.size[1]
            img = img.resize((width, height))

        if text is not None and author is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.load('arial.pil')
            quote = f'{text} - {author}'
            draw.text((10, 30), quote, font=font, fill='white')
            img.save(self.output)

            return self.output
