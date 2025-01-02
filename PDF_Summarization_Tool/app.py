import streamlit as st
import os
from utils import *

def main():
    st.set_page_config(page_title='PDF Summerizer')
    st.title("PDF Summerizing Applications")
    st.write('Summerize your files just few seconds')
    st.divider() 
    
    pdf = st.file_uploader("Upload your PDF file",type='pdf')   
    
    submit=st.button('Generate Summary')
    
    os.environ['OPENAI_API_KEY'] = ''
    
    if submit:
        response = summerizer(pdf)
        
    st.subheader('Summary of the PDF')
    st.write(response)
    
if __name__ == '__main__':
    main()