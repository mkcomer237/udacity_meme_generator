"""Take and image and reformat, add a quote, and save."""


from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
from Exceptions import InvalidImageSize, InvalidTextInput


class MemeEngine():
    """Encapsulate the meme generator image resizing and quote generation.

    Resizing opens an image and resizes it to an appropriate size for
    the meme. Add a bunch of methods to do this?

    Ultimately we need to return a file path with the resized and text
    appended meme.
    """

    def __init__(self, out_dir):
        """Initialize with the location to save the memified images.
        
        Also create the directory to store them if it doesn't already exist.
        """
        self.out_dir = out_dir
        Path(out_dir).mkdir(exist_ok=True)

    def make_meme(self, img_path, body, author, width=500, dynamic_out=True):
        """Take in an image file and quote and save it as a meme.

        Also resize and process the image before adding the
        meme text.
        """
        img = Image.open(img_path)

        # Exceptions for issues with the image or soure file
        if img.size[0] < 500:
            raise InvalidImageSize('The source image width '
                                   'must be at least 500 pixels')

        if len(body) > 40:
            raise InvalidTextInput('The quote is too long')

        # Crop the images
        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('./_data/fonts/Papyrus.ttc', size=30)

        # Make the text location dynamic based on the (resized) image size
        h_loc = img.size[0] - 350
        body_vloc = img.size[1] - 75
        author_vloc = img.size[1] - 45

        draw.text((h_loc, body_vloc), body, font=font, fill='white')
        draw.text((h_loc, author_vloc), '- ' + author, font=font, fill='white')

        # Use a static output file or keep the original filename
        file_path = Path(img_path)
        filename, ext = (file_path.stem, file_path.suffix)
        if dynamic_out:
            out_path = self.out_dir + filename.split('.')[0] + '_memed' + ext
        else:
            out_path = self.out_dir + 'memed_img' + ext
        img.save(out_path)

        return out_path
