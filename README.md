# AskOpenAI: CLI Tool
AskOpenAI is a simple, clean, and elegant command-line interface (CLI) tool to interact with OpenAI's chat models, such as GPT-4 and GPT-3.5-turbo, directly from your terminal. I made this in a few minutes after looking for something like it and not finding anything. What makes this tool so elegant is the use of the `ask` command, unused elsewhere in Linux or Mac; as well as the minimal code. The Python file only contains 840 Bytes, meaning that it ocupies virtually no resources and any delay between prompt and response is contained only to your ping and the OpenAI response time. The use of the `ask` keyword makes this tool feel like something that has been missing in my linux installations all along. I primarily use it for answering one-off questions relating to System Administration or Python developement and I have found it very quick and intuitive to use inbetween commands or in a TMUX terminal. This guide provides instructions for setting up and using the tool on Linux and Mac systems. Windows setup not included because I don't like Windows.
## Installation
### Step 1: Clone the Repository Clone your repository to your local system.
In your terminal, run:
```sh
git clone https://github.com/CollOfTheWild/AskOpenAI.git
cd AskOpenAI
```
### Step 2: Install the OpenAI Python Package
You'll need to install the OpenAI Python package to interact with the API. You can install it using pip:
```sh
pip3 install openai
```
### Step 3: Add Your API Key
Before you can use the tool, you'll need to add your OpenAI API key to the script. Open the script in a text editor:
```sh
nano openai_cli.py
```
Find the line that says:
```python
openai.api_key = "your-api-key-here"
```
Replace `your-api-key-here` with your actual API key, save the file and exit the editor.
## Script
Here is the Python script that makes up the core of the CLI tool:
```python
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

```
## Setup
### Step 1: Move the Script to a System-wide Location
Move the script to a directory in the system's PATH, such as `/usr/local/bin` for Linux and Mac. Rename it to `ask` during the move:
```sh
sudo cp openai_cli.py /usr/local/bin/ask
```
### Step 2: Make the Script Executable Ensure the script is executable:
```sh
sudo chmod +x /usr/local/bin/ask
```
## Usage To use the tool, simply use the `ask` command followed by your query enclosed in single quotes:
```sh
ask 'Your question here'
```
The tool will then communicate with the OpenAI API and return the response directly in the terminal.

## Security Note
Remember to keep your API key secure. Avoid exposing it in public scripts or repositories. Always store your API key in a secure location.
