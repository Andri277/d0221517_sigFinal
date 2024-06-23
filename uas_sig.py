import streamlit as st
from PIL import Image

# Menampilkan judul/heading
st.title("Kepadatan Penduduk Desa KEC.Banggae")

# Path gambar
image_path = 'images/FINAL_SIG.png'

# Load gambar
image = Image.open(image_path)

# Tampilkan gambar menggunakan Streamlit
st.image(image, caption='Gambar Peta')

# Tempat untuk menulis teks
st.write("Peta ini menunjukkan jumlah penduduk dari desa yang ada di kecamatan banggae kab.majene provinsi sulawesi barat.")
