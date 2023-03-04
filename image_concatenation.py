from PIL import Image

def concat(image, raw_palette, bg = (256, 256,256)):
	palette = raw_palette.resize((raw_palette.width * ((image.height // 5) // raw_palette.width), image.height))
	final = Image.new ('RGB', (image.width + palette.width, max(image.height, palette.height)), bg)
	final.paste(image, (0, 0))
	final.paste(palette, (image.width, 0))
	return final