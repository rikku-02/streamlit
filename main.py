import img2pdf
from streamlit_player import st_player
import streamlit as st
from PIL import Image, ImageDraw, ImageFont, ImageOps

st_player("https://www.youtube.com/watch?v=mPWjrD9-hXk")
st.image('https://owo.whats-th.is/3pBJaga.png')
st.title('Text Logo Maker by Rikkuチャン')

font_style = st.selectbox('Font Style フォント・スタイル :', (
    'Dream_Catcher', 'Nyctographic', 'Thunderblack', 'Perpetrator_Italic', 'Perpetrator_Regular', 'Sparkles',
    'Translator'))
font_Size = st.number_input('Font Size フォント・サイズ : ', min_value=None, max_value=None, value=50)
width = st.number_input('Canvas Width キャンバス・ウィツ [ CM ]: ', min_value=None, max_value=None, value=10)
height = st.number_input('Canvas Height キャンバス・ハイト [ CM ]: ', min_value=None, max_value=None, value=5)
DPI = st.slider('DPI ディー・ピー・アイ [ Default: 300 DPI ]:', 72, 600, 300)
bg_color = st.color_picker('Background Color バクグラウンド・カラー :', '#fff')
font_color = st.color_picker('Font Color フォント・カラー :', '#000')
border_color = st.color_picker('Border Color ボーダー・カラー :', '#000')
border_weight = st.slider('Border Weight ボーダー・ウェート [0 = No Border]:', 0, 10, 2)
txt = st.text_input('Text テクスト : ')
build = st.button('Build ビルド →')

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
    pick_font = f'Fonts/{font_style + ".ttf"}'
    font = ImageFont.truetype(pick_font, int(font_size / (res_y_old / res_y)))
    # x, y = (int(x_cm / f * res_x), int(y_cm / f * res_y))
    draw.text(xy=(img.size[0] / 2, img.size[1] / 2), text=txt, font=font, fill=font_color, anchor='mm')


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

st.title('For Image Concatenation')
vertical_row = st.number_input('Number of rows in Vertical: ', min_value=None, max_value=None, value=1)
horizontal_row = st.number_input('Number of rows in Horizontal: ', min_value=None, max_value=None, value=1)
btn1 = st.button('Concatenate Image')
if btn1:
    try:
        with st.spinner('Concatenating...'):
            img_c = Image.open(txt + '.png')
            im_s = img_c.resize((img_c.width // 2, img_c.height // 2))
            get_concat_tile_repeat(im_s, vertical_row, horizontal_row).save('concat.jpg')
            st.image('concat.jpg')

            with open(txt + '.pdf', "wb") as f:
                f.write(img2pdf.convert('concat.jpg'))

            with open(txt + '.pdf', "rb") as pdf_file:
                PDF = pdf_file.read()

                st.download_button(label="Download PDF",
                                   data=PDF,
                                   file_name=txt + '.pdf',
                                   mime='application/octet-stream')

    except ValueError:
        st.warning('0 Value is not allowed to concatinate the image.')
    except FileNotFoundError:
        st.warning('Please Build your image first!')

