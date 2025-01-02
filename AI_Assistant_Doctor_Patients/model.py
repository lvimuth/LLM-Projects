import os
import google.generativeai as genai
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()

google_gemini_api_key=os.getenv("google_gemini_api_key")

genai.configure(api_key=os.environ["google_gemini_api_key"])

def upload_to_gemini(path, mime_type=None):
  """Uploads the given file to Gemini.

  See https://ai.google.dev/gemini-api/docs/prompting_with_media
  """
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)

# TODO Make these files available on the local file system
# You may need to update the file paths


# files = [
#   upload_to_gemini("images.jpeg", mime_type="image/jpeg"),
# ]



# chat_session = model.start_chat(
#   history=[
#     {
#       "role": "user",
#       "parts": [
#         file,
#         "By reading this image diagnosis the the image and describe as a doctor  suggest the what kind of deases has and what are the other possible symptom and what need to do as treatment. provide only this resopnse no need \"Certainly, let's analyze the image and discuss the potential diagnosis, symptoms, and treatment.\"",
#       ],
#     },
#     {
#       "role": "model",
#       "parts": [
#         "Based on the image provided, the prominent lesion on the lower lip appears to be consistent with a squamous cell carcinoma (SCC). Here's a breakdown of the analysis, potential symptoms, and treatment approach:\n\n**Analysis:**\n\n*   **Appearance:** The lesion is raised, has an irregular shape, and exhibits a reddish-pink color with areas of ulceration and a crusted appearance. This is typical of SCC.\n*   **Location:** The lower lip is a common site for SCC, particularly in individuals with sun exposure.\n*   **Features:** The presence of ulceration, crusting, and induration (firmness) are indicative of a potentially malignant process.\n\n**Potential Symptoms:**\n\n*   **Primary Symptom:** A non-healing sore, ulcer, or growth on the lip. This might start as a small, painless nodule, and over time, it can grow and potentially ulcerate.\n*   **Pain or Discomfort:** Some individuals may experience localized pain, tenderness, or a burning sensation.\n*   **Bleeding:** The lesion may bleed easily, especially if it's irritated or traumatized.\n*   **Changes in Texture:** The area may become thickened, scaly, or develop crusting.\n*   **Numbness or Tingling:** If the lesion involves the nerve, there may be associated numbness or tingling in the area.\n*   **Swollen Lymph Nodes:** In later stages or with metastatic spread, the lymph nodes in the neck may become swollen.\n\n**Treatment:**\n\nThe treatment for SCC of the lip depends on the size, location, and depth of the tumor, as well as the individual's overall health. Possible treatment strategies include:\n\n1.  **Surgical Excision:** This is often the primary treatment, especially for small to medium-sized tumors. It involves removing the tumor along with a margin of surrounding healthy tissue. The surgical defect may require reconstruction.\n\n2.  **Mohs Micrographic Surgery:** This technique can be used if the margins of the tumor are difficult to assess. This is a skin-sparing surgical technique that involves sequential removal of layers of tissue and microscopic examination of the margins until a tumor-free margin is achieved.\n\n3.  **Radiation Therapy:** This may be used as a primary treatment if surgery is not feasible, or as an adjuvant therapy after surgery to eradicate any remaining tumor cells.\n\n4.  **Chemotherapy:** May be used in conjunction with radiation therapy or for advanced, metastatic disease.\n\n5.  **Targeted Therapy or Immunotherapy:** For advanced disease, targeted therapy or immunotherapy may be an option, especially if traditional treatments are not successful.\n\n**Recommendations:**\n\n*   **Biopsy:** A biopsy must be performed to confirm the diagnosis and classify the SCC.\n*   **Staging:** Once the biopsy is done, staging studies (physical exam, possibly imaging) should be performed to evaluate the extent of the disease.\n*   **Referral:** A referral to an oral maxillofacial surgeon, dermatologist, or oncologist experienced in the management of SCC of the lip is necessary.\n*   **Sun Protection:** After treatment, lifelong sun protection of the lip is critical to prevent new lesions.\n\n**Important Note:** This information is for educational purposes and is not a substitute for professional medical advice. It is crucial to consult with a qualified healthcare professional for a diagnosis and treatment plan.\n",
#       ],
#     },
#   ]
# )

# response = chat_session.send_message("INSERT_INPUT_HERE")

# print(response.text)