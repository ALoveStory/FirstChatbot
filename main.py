"""
Learning building python chatbot
https://www.youtube.com/watch?v=q5HiD5PNuck - initial tutorial worked as of 10.2023
"""

import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

def chat_with_gtp(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye", "q"]:
            break

        response = chat_with_gtp(user_input)
        print("Chatbot: ", response)
