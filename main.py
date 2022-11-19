import streamlit as st
import owo
import qrcode

def auth():
    k = st.empty()
    priv_key = k.text_input('Private Key:', type="password")
    key = st.secrets['USAGE_KEY']

    if priv_key == key:
        k.empty()
        st.success('Success.')
        main()


def main():
    # File Uploader
    try:
        key = st.secrets['API_KEY']

        st.header('RIKU.File Upload and Url Shortener')

        IMAGE_URL = "https://ahegao.b-cdn.net/wp-content/uploads/2021/04/Ijiranaide-Nagatoro-san-Episode-1-Nagatoro-Wipes-More-Senpai-Tears.jpg"
        st.image(IMAGE_URL)

        st.subheader('RIKU.File Upload')
        uploaded_files = st.file_uploader("Upload File:", accept_multiple_files=True)

        btnUp = st.button('Upload')

        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            with open(f'{uploaded_file.name}', 'wb') as f:
                f.write(bytes_data)

            if btnUp:
                with st.spinner('Uploading...'):
                    link = owo.upload_files(key, uploaded_file.name)
                    st.write(link)
                    qr_img = qrcode.make(link[uploaded_file.name])  
                    qr_img.save('qr.png')
                    st.image('qr.png')
                    st.success('File Uploaded.')
                    

    except UnboundLocalError:
        st.warning('Please select a file.')

    # URL Shortener
    st.subheader('RIKU.URL Shortener')
    url = st.text_input('ex. https://...', '')
    btn = st.button('Shorten')
    req = 'https://'
    dot = '.'

    if len(url) <= 8 or dot not in url:
            if btn:
                st.warning('Please input a URL.')

    else:
        try:
            if req in url:
                if btn:
                    link_s = owo.shorten_urls(key, url)
                    st.write(link_s)
                    qr_img1 = qrcode.make(link_s[0])  
                    qr_img1.save('qr1.png')
                    st.image('qr1.png')
        
            elif req not in url:
                if btn:
                    link_s = owo.shorten_urls(key, req + url)
                    st.write(link_s)
                    qr_img1 = qrcode.make(link_s[0])  
                    qr_img1.save('qr1.png')
                    st.image('qr1.png')


        

        except ValueError:
            pass


if __name__ == '__main__':
    main()
