import streamlit as st
from PIL import Image, ImageDraw, ImageFont, ImageOps
import img2pdf


def app():
    with st.expander('Text Design: '):
        col1, col2, col3 = st.columns(3)

        with col1:
            st.header('Text Style')
            font_style = st.selectbox('Font Style:', ('Dream_Catcher', 'Nyctographic', 'Thunderblack', 'Perpetrator_Italic', 'Perpetrator_Regular',
                'Sparkles',
                'Translator', 'Sakurata'))
            font_Size = st.number_input('Font Size: ', min_value=None, max_value=None, value=20)
            font_color = st.color_picker('Font Color:', '#fff')

        with col2:
            st.header('Dimension')
            width = st.number_input('Canvas Width [ CM ]: ', min_value=None, max_value=None, value=2.0)
            height = st.number_input('Canvas Height [ CM ]: ', min_value=None, max_value=None, value=1.0)
            DPI = st.number_input('DPI [ Default: 300 DPI ]:', min_value=None, max_value=None, value=300)

        with col3:
            st.header('Layout')
            bg_color = st.color_picker('Background Color:', '#000')

            border_color = st.color_picker('Border Color:', '#fff')
            border_weight = st.slider('Border Weight [0 = No Border]:', 0, 20, 2)

        with st.container():
            txt = st.text_input('Your Text: ')
            build = st.button('Build →')

            # Set up parameters
            w_cm, h_cm = (width, height)  # Real label size in cm
            res_x, res_y = (DPI, DPI)  # Desired resolution
            res_y_old = 94  # Old y resolution (204 / 5.5 * 2.54)

            # Inch-to-cm factor
            f = 2.54

            # Determine image size w.r.t. resolution
            w = int(w_cm / f * res_x)
            h = int(h_cm / f * res_y)

            # Create new image with proper size
            img = Image.new('RGB', (w, h), color=bg_color)
            img_with_border = ImageOps.expand(img, border=border_weight, fill=border_color)

            # Draw elements
            draw = ImageDraw.Draw(img_with_border)

            def draw_text(font_size):
              try:
                  pick_font = f'Fonts/{font_style + ".ttf"}'
                  font = ImageFont.FreeTypeFont(pick_font, int(font_size / (res_y_old / res_y)))
                  # x, y = (int(x_cm / f * res_x), int(y_cm / f * res_y))
                  draw.text(xy=(img.size[0] / 2, img.size[1] / 2), text=txt, font=font, fill=font_color, anchor='mm')
              except:
                pick_font = f'Fonts/{font_style + ".otf"}'
                font = ImageFont.FreeTypeFont(pick_font, int(font_size / (res_y_old / res_y)))
                # x, y = (int(x_cm / f * res_x), int(y_cm / f * res_y))
                draw.text(xy=(img.size[0] / 2, img.size[1] / 2), text=txt, font=font, fill=font_color, anchor='mm')

            if build:
                try:
                    with st.spinner('Chotto Matte チョットー・マット...'):

                        # Draw texts
                        draw_text(font_Size)
                        # Save images
                        img_with_border.save(txt + '.png', dpi=(res_x, res_y))
                        st.image(txt + '.png')
                        with open(txt + '.png', "rb") as file:
                            st.download_button(
                                label="Download",
                                data=file,
                                file_name=txt + '.png',
                                mime="image/png"
                            )

                except (ZeroDivisionError, ValueError, SystemError):
                    if txt == '':
                        st.warning('Input Text Field')
                    else:
                        st.warning('Input Valid Parameters')

    with st.expander("Concatenate Image: "):

        # A4 Size
        page_A4_w = 21
        page_A4_h = 29.70

        # Letter Size
        page_letter_w = 21.59
        page_letter_h = 27.94

        # Legal Size
        page_legal_w = 21.59
        page_legal_h = 33.02

        # Custom Size
        page_custom_w = 0.00
        page_custom_h = 0.00

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

        def superimpose():
            img1 = Image.open("concatenated.png")
            img_w, img_h = img1.size
            background = Image.open(page_type + '.png')
            bg_w, bg_h = background.size
            offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
            background.paste(img1, offset)
            background.save(txt + '_concat' + '.png', format='PNG')

        col_c, col_c2 = st.columns(2)

        with col_c:
            st.subheader('Concatenation:')
            page_type = st.selectbox('Page Type:', ('A4', 'Letter', 'Legal', 'Custom'))

            if page_type == 'A4':
                width_bg = st.number_input('Canvas Width [ CM ]: ', min_value=None, max_value=None, value=page_A4_w, disabled=True)
                height_bg = st.number_input('Canvas Height [ CM ]: ', min_value=None, max_value=None, value=page_A4_h, disabled=True)
                vertical_row = st.number_input('Vertical Rows: ', min_value=None, max_value=None, value=1)
                horizontal_row = st.number_input('Horizontal Rows: ', min_value=None, max_value=None,
                                                 value=1)

                # Set up parameters
                w_cm_bg, h_cm_bg = (width_bg, height_bg)  # Real label size in cm
                res_x_bg, res_y_bg = (DPI, DPI)  # Desired resolution

                # Inch-to-cm factor
                f = 2.54

                # Determine image size w.r.t. resolution
                w_bg = int(w_cm_bg / f * res_x_bg)
                h_bg = int(h_cm_bg / f * res_y_bg)

                # Create new image with proper size
                img_bg = Image.new('RGB', (w_bg, h_bg), color="#fff")
                draw = ImageDraw.Draw(img_bg)

                concat_A4 = st.button('Concatenate')

                try:
                    open(txt + '.png', "rb")

                except FileNotFoundError:
                    st.warning('Build your text design first!')

                else:
                    if concat_A4:
                        img_bg.save(page_type + '.png', dpi=(res_x_bg, res_y_bg))

                        img_concat = Image.open(txt + '.png')

                        im_s = img_concat.resize((img_concat.width // 1, img_concat.height // 1))
                        get_concat_tile_repeat(im_s, vertical_row, horizontal_row).save('concatenated.png',
                                                                                        format='PNG')

                        superimpose()

            if page_type == 'Letter':
                width_bg_letter = st.number_input('Canvas Width [ CM ]: ', min_value=None, max_value=None,
                                                  value=page_letter_w, disabled=True)
                height_bg_letter = st.number_input('Canvas Height [ CM ]: ', min_value=None, max_value=None,
                                                   value=page_letter_h, disabled=True)

                vertical_row = st.number_input('Vertical Rows: ', min_value=None, max_value=None, value=1)
                horizontal_row = st.number_input('Horizontal Rows: ', min_value=None, max_value=None,
                                                 value=1)

                # Set up parameters
                w_cm_bg_letter, h_cm_bg_letter = (width_bg_letter, height_bg_letter)  # Real label size in cm
                res_x_bg_letter, res_y_bg_letter = (DPI, DPI)  # Desired resolution

                # Inch-to-cm factor
                f = 2.54

                # Determine image size w.r.t. resolution
                w_bg_letter = int(w_cm_bg_letter / f * res_x_bg_letter)
                h_bg_letter = int(h_cm_bg_letter / f * res_y_bg_letter)

                # Create new image with proper size
                img_bg_letter = Image.new('RGB', (w_bg_letter, h_bg_letter), color="#fff")
                draw = ImageDraw.Draw(img_bg_letter)

                concat_letter = st.button('Concatenate')
                if concat_letter:
                    try:
                        open(txt + '.png', "rb")

                    except FileNotFoundError:
                        st.warning('Build your text design first!')

                    else:
                        img_bg_letter.save(page_type + '.png', dpi=(res_x_bg_letter, res_y_bg_letter))

                        img_concat = Image.open(txt + '.png')

                        im_s = img_concat.resize((img_concat.width // 1, img_concat.height // 1))
                        get_concat_tile_repeat(im_s, vertical_row, horizontal_row).save('concatenated.png',
                                                                                        format='PNG')

                        superimpose()

            if page_type == 'Legal':
                width_bg = st.number_input('Canvas Width [ CM ]: ', min_value=None, max_value=None, value=page_legal_w, disabled=True)
                height_bg = st.number_input('Canvas Height [ CM ]: ', min_value=None, max_value=None, value=page_legal_h, disabled=True)
                vertical_row = st.number_input('Vertical Rows: ', min_value=None, max_value=None, value=1)
                horizontal_row = st.number_input('Horizontal Rows: ', min_value=None, max_value=None,
                                                 value=1)

                # Set up parameters
                w_cm_bg, h_cm_bg = (width_bg, height_bg)  # Real label size in cm
                res_x_bg, res_y_bg = (DPI, DPI)  # Desired resolution

                # Inch-to-cm factor
                f = 2.54

                # Determine image size w.r.t. resolution
                w_bg = int(w_cm_bg / f * res_x_bg)
                h_bg = int(h_cm_bg / f * res_y_bg)

                # Create new image with proper size
                img_bg = Image.new('RGB', (w_bg, h_bg), color="#fff")
                draw = ImageDraw.Draw(img_bg)

                concat_legal = st.button('Concatenate')

                try:
                    open(txt + '.png', "rb")

                except FileNotFoundError:
                    st.warning('Build your text design first!')

                else:
                    if concat_legal:
                        img_bg.save(page_type + '.png', dpi=(res_x_bg, res_y_bg))

                        img_concat = Image.open(txt + '.png')

                        im_s = img_concat.resize((img_concat.width // 1, img_concat.height // 1))
                        get_concat_tile_repeat(im_s, vertical_row, horizontal_row).save('concatenated.png',
                                                                                        format='PNG')

                        superimpose()

            if page_type == 'Custom':
                width_bg = st.number_input('Canvas Width [ CM ]: ', min_value=None, max_value=None, value=page_custom_w)
                height_bg = st.number_input('Canvas Height [ CM ]: ', min_value=None, max_value=None, value=page_custom_h)
                vertical_row = st.number_input('Vertical Rows: ', min_value=None, max_value=None, value=1)
                horizontal_row = st.number_input('Horizontal Rows: ', min_value=None, max_value=None,
                                                 value=1)

                # Set up parameters
                w_cm_bg, h_cm_bg = (width_bg, height_bg)  # Real label size in cm
                res_x_bg, res_y_bg = (DPI, DPI)  # Desired resolution

                # Inch-to-cm factor
                f = 2.54

                # Determine image size w.r.t. resolution
                w_bg = int(w_cm_bg / f * res_x_bg)
                h_bg = int(h_cm_bg / f * res_y_bg)

                # Create new image with proper size
                img_bg = Image.new('RGB', (w_bg, h_bg), color="#fff")
                draw = ImageDraw.Draw(img_bg)

                concat_custom = st.button('Concatenate')

                try:
                    open(txt + '.png', "rb")

                except FileNotFoundError:
                    st.warning('Build your text design first!')

                else:
                    try:
                        if concat_custom:
                            img_bg.save(page_type + '.png', dpi=(res_x_bg, res_y_bg))

                            img_concat = Image.open(txt + '.png')

                            im_s = img_concat.resize((img_concat.width // 1, img_concat.height // 1))
                            get_concat_tile_repeat(im_s, vertical_row, horizontal_row).save('concatenated.png',
                                                                                            format='PNG')

                            superimpose()

                    except SystemError:
                        st.warning('Page Layout is smaller than the object.')

        with col_c2:
            try:
                st.subheader('Output:')
                st.image(txt + '_concat' + '.png')

                with open(txt + '.pdf', "wb") as f:
                    f.write(img2pdf.convert(txt + '_concat' + '.png'))

                with open(txt + '.pdf', "rb") as pdf_file:
                    PDF = pdf_file.read()

                    st.download_button(label="Download PDF",
                                       data=PDF,
                                       file_name=txt + '.pdf',
                                       mime='application/octet-stream')

            except FileNotFoundError:
                st.info('Output will show here.')

