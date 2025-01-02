import streamlit as st
from pathlib import Path
import google.generativeai as genai


#Set the page configuration
st.set_page_config(page_title='VitalImage Analytics',page_icon=':robot:')

#Set the logo
st.image('logo.png',width=100)

st.title('🩺 VitalImage Analytics 📊')

st.subheader('🔍 An application that helps users identify diseases using medical images 🖼️')


uploaded_file = st.file_uploader('Upload an image',type=['png','jpg','jpeg'])

submit_button = st.button('Generate the Analysis')

if submit_button:
    if uploaded_file is None:
        st.error('No file uploaded.')
        # st.warning('This is a warning', icon="⚠️")
    else:
        pass