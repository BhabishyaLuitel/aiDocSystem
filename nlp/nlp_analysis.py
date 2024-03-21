import os
import openai
from dotenv import load_dotenv
from data_processing.processor import clean_text

# Load environment variables
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def analyze_text_with_chat_gpt(text):
    """Generates a concise explanation for the commit message."""
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": text}
            ]
        )
        # Correctly accessing the response content
        if response.choices:
            message_content = response.choices[0].message.content
            return message_content.strip()
        else:
            return "No response generated."
    except Exception as e:
        return f"An error occurred: {e}"
