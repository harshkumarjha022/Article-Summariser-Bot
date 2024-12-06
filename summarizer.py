import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# Configure the Gemini API key
def configure_api():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")
    genai.configure(api_key=api_key)

# Function to summarize text using Gemini API
def summarize_text(content, max_sentences=3):
    try:
        # configure_api()  # Set up API key for authentication
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        prompt = "Summarize the given text in detail in para form"
        response = model.generate_content([prompt, content])
        # Extract and return the generated text
        return response.text if response else "No summary generated."
    except Exception as e:
        print(f"Error during summarization: {e}")
        return "Failed to generate summary."
