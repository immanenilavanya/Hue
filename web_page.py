#The web app interface
from PIL import Image
from io import BytesIO
import streamlit as st
import palette_extraction as pe
import image_concatenation as ic

@st.cache
def to_bytes(image):
	buf = BytesIO()
	image.save(buf, format = "PNG")
	return buf.getvalue()

st.set_page_config(layout="wide", page_title="Hue - A Palette Extractor")
st.write("## Generate a palette from your image")

upload = st.sidebar.file_uploader("Upload an image", type = ["png", "jpg", "jpeg"])

if upload is None:
	uploaded_image = Image.open("sample_image.jpg")
else:
	uploaded_image = Image.open(upload)

col1, col2 = st.columns(2)

col1.write("Uploaded image: ")
col1.image(uploaded_image)
palette_size = col1.slider("Number of colours in the palette", min_value = 1, max_value = 10, value = 8, step = 1)

palette = pe.generate_palette(uploaded_image, palette_size)
col2.write("Generated palette: ")
col2.image(palette)
col2.download_button("Download palette", to_bytes(palette), file_name = "palette.png")
col2.download_button("Download image with palette", to_bytes(ic.concat(uploaded_image, palette), file_name = "combined.png")
