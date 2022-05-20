import streamlit as st
from multiapp import MultiApp
from apps import RN, ytmp3, ytmp4, YTPro

app = MultiApp()
# Dev-R
st.set_page_config(
    page_title="YouTube Converter by Devr-R",
    page_icon="https://cdn3.iconfinder.com/data/icons/e-commerce-35/74/money_conversion-512.png",
    layout='centered',
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://fb.me/devric.ui',
        'Report a bug': "https://fb.me/devric.ui",
        'About': "# Created by Dev-R"
    }
)

st.image('https://owo.whats-th.is/6JbgvJX.png')


app.add_app("Release Notes", RN.app)
app.add_app("Convert to Mp3", ytmp3.app)
app.add_app("Convert to Mp4", ytmp4.app)
app.add_app("YouTube Pro", YTPro.app)

app.run()
