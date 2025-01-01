import streamlit as st
from model import chat_session,image_session
import streamlit as st
from PIL import Image
from imageGen import client

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
    blog_response = chat_session.send_message(
        f"generate a comprehensive, engaging blog post relevant to the given title and keywords. The blog title is {blog_tittle} and the Keywords are {keywords}.And use {num_images} images to describe the blogs and for the image place holders use [image] The blog should be approximately {num_words} words in length, suitable for an online audience. Make sure to use SEO techniques and subheadings. Ensure the content is original, informative, and maintains a consistent tone throughout. Generate only the content without any explanation.The heading should be in bold, and the subheadings should be in medium bold."
    )
    
    
    image_response = image_session.send_message(f"'{blog_response.parts[0].text}' summerize this blog post and generate a prompt to generate an image using hugging face to add in to the above mention blog post. give me only the Image Prompt as output. image should be realisitc natural 3d")
    
    
    # image_prompt = image_response.parts[0].text.split("\n\n**Image Prompt:**\n\n")[1]

    image = client.text_to_image(image_response.parts[0].text)
    
    # Display the PIL.Image object in Streamlit
    st.image(image, use_column_width=True)


    st.write(blog_response.parts[0].text)