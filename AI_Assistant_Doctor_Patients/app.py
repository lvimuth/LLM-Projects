import streamlit as st
from pathlib import Path
from model import upload_to_gemini,model
import os

# Set the page configuration
st.set_page_config(page_title='VitalImage Analytics', page_icon=':robot:')

# Set the logo
st.image('logo.png', width=100)

st.title('🩺 VitalImage Analytics 📊')
st.subheader('🔍 An application that helps users identify diseases using medical images 🖼️')

uploaded_file = st.file_uploader('Upload an image', type=['png', 'jpg', 'jpeg'])
if uploaded_file:
    st.image(uploaded_file,width=250,caption='Uploaded Medical Image')

submit_button = st.button('Generate the Analysis')

if submit_button:
    if uploaded_file is None:
        st.error('No file uploaded.')
    else:
        # Save the uploaded file
        file_extension = os.path.splitext(uploaded_file.name)[1]  # Gets the extension (e.g., '.jpg', '.png', '.jpeg')
        temp_file_path = f"temp_image{file_extension}"
        
        try:
            with open(temp_file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Pass the file to the model
            file = upload_to_gemini(temp_file_path, mime_type="image/jpeg")
            
            chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        file,
        "By reading this image diagnosis the the image and describe as a doctor  suggest the what kind of deases has and what are the other possible symptom and what need to do as treatment. provide only this resopnse no need \"Certainly, let's analyze the image and discuss the potential diagnosis, symptoms, and treatment.\"",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Based on the image provided, the prominent lesion on the lower lip appears to be consistent with a squamous cell carcinoma (SCC). Here's a breakdown of the analysis, potential symptoms, and treatment approach:\n\n**Analysis:**\n\n*   **Appearance:** The lesion is raised, has an irregular shape, and exhibits a reddish-pink color with areas of ulceration and a crusted appearance. This is typical of SCC.\n*   **Location:** The lower lip is a common site for SCC, particularly in individuals with sun exposure.\n*   **Features:** The presence of ulceration, crusting, and induration (firmness) are indicative of a potentially malignant process.\n\n**Potential Symptoms:**\n\n*   **Primary Symptom:** A non-healing sore, ulcer, or growth on the lip. This might start as a small, painless nodule, and over time, it can grow and potentially ulcerate.\n*   **Pain or Discomfort:** Some individuals may experience localized pain, tenderness, or a burning sensation.\n*   **Bleeding:** The lesion may bleed easily, especially if it's irritated or traumatized.\n*   **Changes in Texture:** The area may become thickened, scaly, or develop crusting.\n*   **Numbness or Tingling:** If the lesion involves the nerve, there may be associated numbness or tingling in the area.\n*   **Swollen Lymph Nodes:** In later stages or with metastatic spread, the lymph nodes in the neck may become swollen.\n\n**Treatment:**\n\nThe treatment for SCC of the lip depends on the size, location, and depth of the tumor, as well as the individual's overall health. Possible treatment strategies include:\n\n1.  **Surgical Excision:** This is often the primary treatment, especially for small to medium-sized tumors. It involves removing the tumor along with a margin of surrounding healthy tissue. The surgical defect may require reconstruction.\n\n2.  **Mohs Micrographic Surgery:** This technique can be used if the margins of the tumor are difficult to assess. This is a skin-sparing surgical technique that involves sequential removal of layers of tissue and microscopic examination of the margins until a tumor-free margin is achieved.\n\n3.  **Radiation Therapy:** This may be used as a primary treatment if surgery is not feasible, or as an adjuvant therapy after surgery to eradicate any remaining tumor cells.\n\n4.  **Chemotherapy:** May be used in conjunction with radiation therapy or for advanced, metastatic disease.\n\n5.  **Targeted Therapy or Immunotherapy:** For advanced disease, targeted therapy or immunotherapy may be an option, especially if traditional treatments are not successful.\n\n**Recommendations:**\n\n*   **Biopsy:** A biopsy must be performed to confirm the diagnosis and classify the SCC.\n*   **Staging:** Once the biopsy is done, staging studies (physical exam, possibly imaging) should be performed to evaluate the extent of the disease.\n*   **Referral:** A referral to an oral maxillofacial surgeon, dermatologist, or oncologist experienced in the management of SCC of the lip is necessary.\n*   **Sun Protection:** After treatment, lifelong sun protection of the lip is critical to prevent new lesions.\n\n**Important Note:** This information is for educational purposes and is not a substitute for professional medical advice. It is crucial to consult with a qualified healthcare professional for a diagnosis and treatment plan.\n",
      ],
    },
  ])
            response = chat_session.send_message("By reading this image diagnosis the the image and describe as a doctor  suggest the what kind of deases has and what are the other possible symptom and what need to do as treatment. provide only this resopnse no need \"Certainly, let's analyze the image and discuss the potential diagnosis, symptoms, and treatment.\"")

            # st.text(response)
            if response:
                st.title("Here is the analysis based on your Image:")
                st.write(response.parts[0].text)
            
        except Exception as e:
            st.error(f"An error occurred: {e}")

        finally:
            # Delete the temporary file
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)
