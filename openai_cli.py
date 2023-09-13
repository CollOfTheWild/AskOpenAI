#!/usr/bin/env python3

import openai
import sys

openai.api_key = "your-api-key-here"

def main():
    if len(sys.argv) < 2:
        print("Usage: ask [-t topic] Your message here")
        sys.exit(1)

    # Initialize with default system message
    system_message = "You are a helpful assistant."

    # Check for the -t flag
    if '-t' in sys.argv:
        topic_index = sys.argv.index('-t')
        if topic_index + 1 < len(sys.argv):  # Ensure there's a topic after -t
            topic = sys.argv[topic_index + 1]
            system_message = f"You are a helpful assistant in all things regarding {topic}."
            # Remove the -t flag and topic from sys.argv
            del sys.argv[topic_index:topic_index+2]
        else:
            print("Error: Missing topic after -t flag.")
            sys.exit(1)

    user_message_content = ' '.join(sys.argv[1:])

    messages = [
        {"role": "system", "content": system_message},
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
