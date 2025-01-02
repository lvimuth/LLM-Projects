import streamlit as st
import os

def main():
    st.set_page_config(page_title='PDF Summerizer')
    st.title("PDF Summerizing Applications")
    st.write('Summerize your files just few seconds')
    st.divider() 
    
    st.file_uploader("Upload your PDF file",type='pdf')   
    
    submit=st.button('Generate Summary')
    
if __name__ == '__main__':
    main()