import streamlit as st
import img2pdf


uploaded_files = st.file_uploader("Upload File:", accept_multiple_files=True)

btnUp = st.button('Upload')

for uploaded_file in uploaded_files:
  bytes_data = uploaded_file.read()
  with open(f'{uploaded_file.name}', 'wb') as f:
                f.write(bytes_data)


if btnUp:
  with st.spinner('Uploading...'):
    with open("sample.pdf","wb") as f:
	    f.write(img2pdf.convert(uploaded_file.name))
    
    with open("sample.pdf", "rb") as pdf_file:
      PDFbyte = pdf_file.read()

      st.download_button(label="Download", 
                       data=PDFbyte,
                       file_name="Output.pdf",
                       mime='application/octet-stream')