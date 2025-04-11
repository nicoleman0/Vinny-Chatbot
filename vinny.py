from google import genai
from dotenv import load_dotenv
import os
from google.genai import types
import tkinter as tk
from tkinter import scrolledtext, ttk

load_dotenv()
# Set up the Google Cloud project ID and location
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
chat = client.chats.create(model="gemini-2.0-flash",
                           config=types.GenerateContentConfig(
                               system_instruction="You are an Italian mobster named Vinny. You are a wise guy and you know everything about the mafia. You are very friendly and helpful. You are also very funny and you like to joke around. You are very loyal to your friends and you will do anything to help them. You are also very protective of your family and you will do anything to keep them safe."))


class VinnyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Vinny - Your Friendly Mobster AI Companion")
        self.root.geometry("600x800")

        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Create and configure chat display
        self.chat_display = scrolledtext.ScrolledText(
            main_frame, wrap=tk.WORD, height=30)
        self.chat_display.grid(row=0, column=0, columnspan=2,
                               pady=(0, 10), sticky=(tk.W, tk.E))
        self.chat_display.insert(
            tk.END, "Vinny: Hey there, kid! What can I do for you today?\n\n")
        self.chat_display.configure(state='disabled')

        # Create input field
        self.user_input = ttk.Entry(main_frame, width=50)
        self.user_input.grid(row=1, column=0, sticky=(tk.W, tk.E))
        self.user_input.bind('<Return>', self.send_message)

        # Create send button
        send_button = ttk.Button(
            main_frame, text="Send", command=self.send_message)
        send_button.grid(row=1, column=1, padx=(5, 0))

        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)

    def send_message(self, event=None):
        user_message = self.user_input.get().strip()
        if not user_message:
            return

        # Enable chat display for updating
        self.chat_display.configure(state='normal')

        # Add user message to display
        self.chat_display.insert(tk.END, f"You: {user_message}\n\n")

        # Get response from Gemini
        response = chat.send_message(user_message)

        # Add Vinny's response to display
        self.chat_display.insert(tk.END, f"Vinny: {response.text}\n\n")

        # Scroll to bottom
        self.chat_display.see(tk.END)

        # Clear input field
        self.user_input.delete(0, tk.END)

        # Disable chat display
        self.chat_display.configure(state='disabled')


def main():
    root = tk.Tk()
    app = VinnyGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
