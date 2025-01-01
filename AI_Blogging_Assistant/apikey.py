from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()
openai_api_key=''
google_gemini_api_key=os.getenv("GOOGLE_GEMINI_API_KEY")

if not google_gemini_api_key:
    raise ValueError("Google Gemini API Key is not set in the .env file!")


