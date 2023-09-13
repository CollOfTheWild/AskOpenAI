#!/usr/bin/env python3

import openai
import sys

openai.api_key = "your-api-key-here"

def main():
    if len(sys.argv) < 2:
        print("Usage: ask 'Your message here'")
        sys.exit(1)

    user_message_content = sys.argv[1]

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_message_content}
    ]

    try:
        completion = openai.ChatCompletion.create(
          model="gpt-4-0613",
          messages=messages
        )
        print(completion.choices[0].message['content'])
    except openai.error.OpenAIError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
