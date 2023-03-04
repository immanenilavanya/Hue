import numpy as np
from PIL import Image
import streamlit as st
from sklearn.cluster import KMeans

@st.cache
def load_image(image):
    image = image.convert('RGB')
    temp = np.array(image).reshape(-1, 3)
    img_unique = np.unique(temp.reshape(-1, 3), axis = 0)
    return img_unique

@st.cache
def get_palette(img_unique, palette_size):
    kmn = KMeans(n_clusters = palette_size, n_init = 10)
    kmn.fit(img_unique)
    palette = kmn.cluster_centers_.round().astype(np.uint8)
    palette_img = Image.fromarray(palette.reshape(-1, 1, 3))
    return palette_img.resize((32, palette_size * 32), Image.Resampling.NEAREST)

def generate_palette(image, palette_size = 8):
    img_unique = load_image(image)
    palette = get_palette(img_unique, palette_size)
    return palette
