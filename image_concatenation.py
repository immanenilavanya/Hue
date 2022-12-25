from PIL import Image

def concat(im1, im2, color=(256, 256, 256)):
    new_width = im1.height // 5
    c = new_width // im2.width
    palette = im2.resize((im2.width * c, im1.height))
    final = Image.new('RGB', (im1.width + palette.width, max(im1.height, palette.height)), color)
    final.paste(im1, (0, 0))
    final.paste(palette, (im1.width, 0))
    return final
