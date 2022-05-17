import streamlit as st
import img2pdf
from PIL import Image
import os


uploaded_files = st.file_uploader("Upload File:", accept_multiple_files=True)

btnUp = st.button('Upload')

for uploaded_file in uploaded_files:
  bytes_data = uploaded_file.read()
  with open(f'{uploaded_file.name}', 'wb') as f:
                f.write(bytes_data)


if btnUp:
  with st.spinner('Uploading...'):
    image = Image.open(uploaded_file.name)
    pdf_path = "file.pdf"
    pdf_bytes = img2pdf.convert(image.filename)

    with open(pdf_path, "rb") as pdf_file:
      PDFbyte = pdf_file.write(pdf_bytes)
      image.close()
      file.close()
    

    with open("file.pdf", "rb") as pdf_file:
      PDFbyte = pdf_file.read()

      st.download_button(label="Download", 
                       data=PDFbyte,
                       file_name="Output.pdf",
                       mime='application/octet-stream')