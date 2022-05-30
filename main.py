import streamlit as st
from multiapp import MultiApp
from app import home, create, custom

app = MultiApp()


st.image('https://owo.whats-th.is/3pBJaga.png')
st.title('Text Logo Maker by Rikkuチャン')

app.add_app("Home", home.app)
app.add_app("Create", create.app)
app.add_app("Upload your Custom Design", custom.app)

# The main app
app.run()