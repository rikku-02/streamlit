import streamlit as st
from PIL import Image



uploaded_files = st.file_uploader("Upload File:", accept_multiple_files=True)

btnUp = st.button('Upload')

for uploaded_file in uploaded_files:
  bytes_data = uploaded_file.read()
  with open(f'{uploaded_file.name}', 'wb') as f:
                f.write(bytes_data)


if btnUp:
  with st.spinner('Uploading...'):
    image_1 = Image.open(uploaded_file.name)
    im_1 = image_1.convert('RGB')
    im_1.save('Output.pdf')

    with open("Output.pdf", "rb") as pdf_file:
      PDFbyte = pdf_file.read()

      st.download_button(label="Download", 
                       data=PDFbyte,
                       file_name="Output.pdf",
                       mime='application/octet-stream')