import streamlit as st

def app():
    code = '''
    def Hello():
        return "Go to Navigation to continue"'''
    st.code(code, language='python')
