import streamlit as st
import owo
from utils import db

conn = db.connect()
comments = db.collect(conn)

with st.expander("💬 Open comments"):

    # Show comments

    st.write("**Comments:**")

    for index, entry in enumerate(comments.itertuples()):
        st.markdown(COMMENT_TEMPLATE_MD.format(entry.name, entry.date, entry.comment))

        is_last = index == len(comments) - 1
        is_new = "just_posted" in st.session_state and is_last
        if is_new:
            st.success("☝️ Your comment was successfully posted.")

    space(2)

    # Insert comment

    st.write("**Add your own comment:**")
    form = st.form("comment")
    name = form.text_input("Name")
    comment = form.text_area("Comment")
    submit = form.form_submit_button("Add comment")

    if submit:
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        db.insert(conn, [[name, comment, date]])
        if "just_posted" not in st.session_state:
            st.session_state["just_posted"] = True
        st.experimental_rerun()

def auth():
    k = st.empty()
    priv_key = k.text_input('Private Key:', type="password")
    key = st.secrets['USAGE_KEY']

    if priv_key == key:
        k.empty()
        st.success('Success.')
        main()  

def main():
    try:
        key = st.secrets['API_KEY']

        st.header('Rikku.File Upload and Url Shortener')
        
        IMAGE_URL = "https://ahegao.b-cdn.net/wp-content/uploads/2021/04/Ijiranaide-Nagatoro-san-Episode-1-Nagatoro-Wipes-More-Senpai-Tears.jpg"
        st.image(IMAGE_URL)


        st.subheader('Rikku.File Upload')
        uploaded_files = st.file_uploader("Upload File:", accept_multiple_files=True)

        btnUp = st.button('Upload')

        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            with open(f'{uploaded_file.name}', 'wb') as f: 
                f.write(bytes_data)
    
        if btnUp:           
            with st.spinner('Uploading...'):
                st.write(owo.upload_files(key, uploaded_file.name))
                st.success('File Uploaded.')
   
    except UnboundLocalError:
        st.warning('Please select a file.')
            
     
               

 
    
#####
    st.subheader('Rikku.URL Shortener')
    url = st.text_input('ex. https://...', '')
    btn = st.button('Shorten')
    req = 'https://'



    try:
        if len(url) > 12:
            if btn:
                st.write(owo.shorten_urls(key, req + url))
                
        if len(url) <= 8:
            if btn:
                st.warning('Please input a URL')
            

    except ValueError:               
        pass
    

if __name__ == '__main__':
    auth()
