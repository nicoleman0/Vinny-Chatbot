# Vinny the Wiseguy

## Overview

This is a simple command-line chat application that lets you interact with "Vinny," a Gemini AI character designed to respond as a mobster from New York. Vinny uses Google's Gemini AI model through the Google AI Python SDK.

## What Vinny Can Do

- Vinny responds as a friendly Italian mobster with wisdom, humor, and loyalty themes
- Command-line interface for easy interaction
- Chat history tracking and display
- Easy to use conversation flow

## Prerequisites

- Python 3.6+
- Google Cloud account with access to the Gemini API
- Gemini API key

## Installing Vinny

1. Clone this repository or download the script

2. Install the required dependencies:
   ```bash
   pip install google-generativeai python-dotenv
   ```

3. Create a `.env` file in the same directory as the script with your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Using Vinny

1. Run the script:
   ```bash
   python vinny.py
   ```

2. The prompt will appear, and you can start chatting with Vinny!

3. After each response:
   - The AI's response will be displayed
   - You'll be asked if you want to continue chatting

4. To exit the chat, respond with anything other than "yes," "y," "ok," "sure," or "continue" when asked if you want to ask another question.

## Example Interaction

```
Ask a question, sonny: Tell me about yourself.

Hey there, how you doin'? The name's Vinny, and I got connections, if you know what I mean. Been in this business for longer than I care to count, capisce? Family's everything to me - would take a bullet for any of my guys. People come to me when they got problems that need... creative solutions. I'm always happy to help a friend, just remember: favors ain't free in this life, but for you? I might make an exception. What else you wanna know about ol' Vinny?