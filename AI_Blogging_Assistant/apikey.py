from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()

google_gemini_api_key=os.getenv("GOOGLE_GEMINI_API_KEY")
huging_face_token=os.getenv('HUGGING_FACE_TOKEN')

if not google_gemini_api_key:
    raise ValueError("Google Gemini API Key is not set in the .env file!")

if not huging_face_token:
    raise ValueError("Hugging Face API Key is not set in the .env file!")


