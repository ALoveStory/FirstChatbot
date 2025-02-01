"""
Learning building python chatbot
https://www.youtube.com/watch?v=q5HiD5PNuck - initial tutorial worked as of 10.2023
Went through documentation to update as of January 2025 - https://platform.openai.com/docs/quickstart
"""

from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def chat_with_gtp(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
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
