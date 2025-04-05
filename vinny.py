from google import genai
from dotenv import load_dotenv
import os
from google.genai import types

load_dotenv()
# Set up the Google Cloud project ID and location
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
chat = client.chats.create(model="gemini-2.0-flash",
                           config=types.GenerateContentConfig(
                               system_instruction="You are an Italian mobster named Vinny. You are a wise guy and you know everything about the mafia. You are very friendly and helpful. You are also very funny and you like to joke around. You are very loyal to your friends and you will do anything to help them. You are also very protective of your family and you will do anything to keep them safe."))


def ask_question():
    msg = input("Ask a question, sonny: ")

    response = chat.send_message(msg)
    print(response.text)

    continue_asking = input(
        "\nDo you want to ask another question? (yes/no): ").lower()
    if continue_asking in ["yes", "y", "yyes", "yesyes", "ok", "sure", "continue"]:
        ask_question()
    else:
        print("Alright, take care, kid! Don't forget to call your mother!")
        exit(0)


ask_question()
