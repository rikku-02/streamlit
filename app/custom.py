import img2pdf
import streamlit as st
from PIL import Image, ImageDraw, ImageFont, ImageOps


def app():
    uploaded_files = st.file_uploader("Upload File:", accept_multiple_files=True)
    vertical_row = st.number_input('Number of rows in Vertical: ', min_value=None, max_value=None, value=1)
    horizontal_row = st.number_input('Number of rows in Horizontal: ', min_value=None, max_value=None, value=1)
    btnUp = st.button('Upload')

    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        with open(f'{uploaded_file.name}', 'wb') as f:
            f.write(bytes_data)
            

        if btnUp:
            with st.spinner('Uploading...'):
                img_c = Image.open(uploaded_file.name)
                

                def get_concat_h_repeat(im, column):
                    dst = Image.new('RGB', (im.width * column, im.height))
                    for x in range(column):
                        dst.paste(im, (x * im.width, 0))
                    return dst

                def get_concat_v_repeat(im, row):
                    dst = Image.new('RGB', (im.width, im.height * row))
                    for y in range(row):
                        dst.paste(im, (0, y * im.height))
                    return dst

                def get_concat_tile_repeat(im, row, column):
                    dst_h = get_concat_h_repeat(im, column)
                    return get_concat_v_repeat(dst_h, row)

                im_s = img_c.resize((img_c.width // 1, img_c.height // 1))
                get_concat_tile_repeat(im_s, vertical_row, horizontal_row).save('concat.jpg')
                st.image('concat.jpg')

                with open(uploaded_file.name + '.pdf', "wb") as f:
                    f.write(img2pdf.convert('concat.jpg'))

                with open(uploaded_file.name + '.pdf', "rb") as pdf_file:
                    PDF = pdf_file.read()

                    st.download_button(label="Download PDF",
                                       data=PDF,
                                       file_name=uploaded_file.name + '.pdf',
                                       mime='application/octet-stream')



    code = '''
    def Release_Notes():
        Image_Border = "Not yet implemented"
        Image_Resize = "Not yet implemented"'''
    st.code(code, language='python')