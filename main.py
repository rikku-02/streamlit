import streamlit as st
import aspose.words as aw



uploaded_files = st.file_uploader("Upload File:", accept_multiple_files=True)

btnUp = st.button('Upload')

for uploaded_file in uploaded_files:
  bytes_data = uploaded_file.read()
  with open(f'{uploaded_file.name}', 'wb') as f:
                f.write(bytes_data)


if btnUp:
  with st.spinner('Uploading...'):
    fileNames = [uploaded_file.name]

    doc = aw.Document()
    builder = aw.DocumentBuilder(doc)

    for fileName in fileNames:
      builder.insert_image(fileName)
    # Insert a paragraph break to avoid overlapping images.
      builder.writeln()

      pdf = doc.save("Output.pdf");
      
      st.download_button(label="Export_Report",
                    data=pdf,
                    file_name="output.pdf",
                    mime='application/octet-stream')