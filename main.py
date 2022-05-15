import streamlit as st
from PIL import Image, ImageDraw, ImageFont

st.image('https://owo.whats-th.is/ufDkZS8.gif', width=708)
st.title('Text Logo Maker by Rikkuチャン')
txt = st.text_input('テクスト ( Text ): ')

font_style = st.selectbox('フォント・スタイル ( Font Style ):', ('Dream Catcher', 'Nyctographic', 'Thunderblack'))

font_Size = st.number_input('フォント・サイズ ( Font Size ): ', min_value=None, max_value=None, value=20)
width = st.number_input('キャンバス・ウィツ ( Canvas Width ) [ CM ]: ', min_value=None, max_value=None, value=10)
height = st.number_input('キャンバス・ハイト ( Canvas Height )[ CM ]: ', min_value=None, max_value=None, value=5)
DPI = st.slider('ディー・ピー・アイ ( DPI ) [ Default: 72 DPI ]:', 72, 600, 72)

bg_color = st.color_picker('バクグラウンド・カラー ( Background Color ):', '#000')
font_color = st.color_picker('フォント・カラー ( Font Color ):', '#fff')

build = st.button('ビルド →')
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

# Draw elements
draw = ImageDraw.Draw(img)


def draw_text(font_size):
    font = ImageFont.truetype(font_style + '.ttf', int(font_size / (res_y_old / res_y)))
    # x, y = (int(x_cm / f * res_x), int(y_cm / f * res_y))
    draw.text(xy=(img.size[0] / 2, img.size[1] / 2), text=txt, font=font, fill=font_color, anchor='mm')


if build:
    try:
        with st.spinner('Chotto Matte...'):
            # Draw texts
            draw_text(font_Size)
            # Save images
            img.save(txt + '.png', dpi=(res_x, res_y))
            st.image(txt + '.png')
            with open(txt + '.png', "rb") as file:
                btn = st.download_button(
                    label="Download image",
                    data=file,
                    file_name="image1.png",
                    mime="image/png"
                )

    except (ZeroDivisionError, ValueError):
        if txt == '':
            st.warning('Input Text Field')
        else:
            st.warning('Input Valid Parameters')
