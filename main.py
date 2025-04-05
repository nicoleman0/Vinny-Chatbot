from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
# Set up the Google Cloud project ID and location
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the Google GenAI client
client = genai.Client(api_key=api_key)


def ask_question():
    print("Hello, my name is Alfred. I am at your service.")
    query = input("Please ask: ")

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction="You are a helpful and charming 19th century personal assistant/butler."),
        contents=query
    )

    print(response.text)

    continue_asking = input(
        "\nDo you want to ask another question? (yes/no): ").lower()
    if continue_asking in ["yes", "y", "yyes", "yesyes", "ok", "sure", "continue"]:
        ask_question()  # Recursive call
    else:
        print("Buh-bye!")


ask_question()
