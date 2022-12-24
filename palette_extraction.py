import numpy as np
from PIL import Image
from sklearn.cluster import KMeans

image_path = "image.jpg"
palette_size = 8
palette_path = "palette.png"

def load_image(path):
   image = Image.open(path).convert('RGB')
   x = np.array(image).reshape(-1, 3) #matrix version of source image
   img_shape = x.shape #to store the shape that can be used to reshape later
   x_unique = np.unique(x.reshape(-1, 3), axis = 0) #to store the unique pixels
   return image, x, x_unique, img_shape

def get_palette(img_unique, palette_size):
    kmn = KMeans(n_clusters = palette_size, n_init = 10)
    kmn.fit(img_unique)
    palette = kmn.cluster_centers_.round().astype(np.uint8)
    palette_img = Image.fromarray(palette.reshape(-1, 1, 3))
    return palette_img.resize((32, palette_size * 32), Image.Resampling.NEAREST)

source_image, matrix, img_unique, img_shape = load_image(image_path)

palette = get_palette(img_unique, palette_size)
palette.save(palette_path)
