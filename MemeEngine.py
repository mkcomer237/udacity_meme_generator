"""Take and image and reformat, add a quote, and save."""


from PIL import Image, ImageDraw, ImageFont


class MemeEngine():
    """Encapsulate the meme generator image resizing and quote generation.

    Resizing opens an image and resizes it to an appropriate size for
    the meme. Add a bunch of methods to do this?

    Ultimately we need to return a file path with the resized and text
    appended meme.
    """

    def __init__(self, out_dir):
        """Initialize with the location to save the memified images."""
        self.out_dir = out_dir

    def make_meme(self, img_path, body, author, width=500):
        """Take in an image file and quote and save it as a meme.

        Also resize and process the image before adding the
        meme text.
        """
        img = Image.open(img_path)

        # Crop the images
        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('./fonts/Papyrus.ttc', size=28)
        draw.text((100, 425), body, font=font, fill='white')
        draw.text((100, 455), '- ' + author, font=font, fill='white')

        # Keep the same filename when outputting
        filename, ext = img_path.split('/')[-1].split('.')
        out_path = self.out_dir + filename.split('.')[0] + '_memed.' + ext
        img.save(out_path)

        return out_path
