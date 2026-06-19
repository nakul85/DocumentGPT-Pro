import os

import streamlit as st

from config import UPLOAD_FOLDER


def ensure_directories():

    folders = [

        UPLOAD_FOLDER,

        "data",

        "chroma_db",

        "assets"

    ]

    for folder in folders:

        os.makedirs(folder, exist_ok=True)


def load_css(file_name):

    with open(file_name) as f:

        st.markdown(

            f"<style>{f.read()}</style>",

            unsafe_allow_html=True
        )