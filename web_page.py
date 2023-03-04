#The web app interface
from PIL import Image
from io import BytesIO
import streamlit as st
import palette_extraction as pe
import image_concatenation as ic

logo = Image.open("Hue.png")

def to_bytes(image):
	buf = BytesIO()
	image.save(buf, format = "PNG")
	return buf.getvalue()

st.set_page_config(layout="wide", page_title="Hue - A Palette Extractor", page_icon = logo, initial_sidebar_state = "expanded")
st.sidebar.image(logo)
st.write("## Generate a palette from your image")

col1, col2 = st.columns(2)

get_upload = st.sidebar.file_uploader("Upload an image", type = ["png", "jpg", "jpeg"])
if get_upload is None:
	uploaded_image = Image.open("sample_image.jpg")
else:
	uploaded_image = Image.open(get_upload)

col1.write("Uploaded image: ")
col1.image(uploaded_image)

palette_size = col1.slider("Number of colours in the palette", min_value = 1, max_value = 10, value = 8, step = 1)
palette_img, palette_hex = pe.generate_palette(uploaded_image, palette_size)
col2.write("Generated palette: ")
col2.image(palette_img)

col2.download_button("Download palette", to_bytes(palette_img), file_name = "palette.png")

st.sidebar.download_button("Download image with palette", to_bytes(ic.concat(uploaded_image, palette_img)), file_name = "combined.png")

st.write("The hex values are: ")
for val in palette_hex:
	st.write(val)
