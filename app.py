import streamlit as st
from ui.interface import render_interface

st.set_page_config(page_title='Estoque GPT', page_icon=":shark:")

if __name__ == "__main__":
    render_interface()
