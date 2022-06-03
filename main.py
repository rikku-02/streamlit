import streamlit as st
from getmac import get_mac_address

mac = get_mac_address()

st.write(mac)
