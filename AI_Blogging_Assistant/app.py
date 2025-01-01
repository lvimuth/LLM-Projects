import streamlit as st

st.set_page_config(layout="wide")
blog = ''
#Title for the application
st.title('📝 BlogCraft: Your AI Writing Companion 🤖')

#Create a subheader
st.subheader('Now you can craft perfect blogs with the help of AI - BlogCraft is your NEW AI BLOG Companion')

#Sidebar for user inputs
with st.sidebar:
    st.title("Input your Blog Details")
    st.subheader("Enter details of the Blog you want to generate")
    
    #Blog Title
    blog_tittle = st.text_input("Blog Title")
    
    #Keywords input
    keywords = st.text_area("Keywords (Comma-Separated words)")
    
    #Number of words
    num_words = st.slider("Number of words",min_value=200,max_value=1000,step=100)
    
    #Number of Images
    num_images = st.number_input("Number of Images",min_value=1,max_value=5,step=1)
    
    #Submit Bitton
    submit_button = st.button("Generate Blog")
    
if submit_button:
    st.image()
    st.write(blog)