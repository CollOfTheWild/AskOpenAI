# AskOpenAI - CLI Tool
AskOpenAI is a simple, clean, and elegant command-line interface (CLI) tool to interact with OpenAI's chat models, such as GPT-4 and GPT-3.5-turbo, directly from your terminal. What makes this tool so elegant is the use of the `ask` command, unused elsewhere in Linux or Mac; as well as the minimal code. The Python script ocupies virtually no resources and any delay between prompt and response is contained only to your network latency and the OpenAI response time. The use of the `ask` keyword makes this tool feel like something that has been missing in my linux installations all along. I primarily use it for answering one-off questions relating to System Administration or Python developement and I have found it very quick and intuitive to use inbetween commands or in a TMUX terminal. This guide provides instructions for setting up and using the tool on Linux and Mac systems. Windows setup not included because I don't like Windows.

## Features

1. **Shell Command Integration**: The tool integrates seamlessly with the shell, allowing you to use the `ask` command directly from the terminal to interact with the OpenAI API. Simply type `ask 'Your question here'` to get a response.

2. **Topic Specification with -t Flag**: The `-t` flag allows you to specify a topic that guides the assistant's responses. Use it in the format `ask -t 'topic' 'Your question here'`. The assistant will then specialize its responses to the specified topic, becoming an expert in that area.

3. **CSV Data Visualization with -g Flag**: The `-g` flag enables you to request Python scripts for data visualization based on a CSV file. Use it in the format `ask -g 'path/to/your/csvfile.csv'`. The tool will interpret the structure of your data and suggest a Python script utilizing the Seaborn library to visualize the data according to Edward Tufte's principles of data visualization. It can adapt the visualization type and color palette based on the nature of the data.

4. **Lightweight and Resource-Efficient**: The Python script is compact and lightweight, occupying minimal disk space and using very little system resources, ensuring fast and efficient operation.

## Usage

```sh
# General usage
ask 'Your question here'

# Specifying a topic with the -t flag
ask -t 'topic' 'Your question here'

# Requesting a data visualization script with the -g flag
ask -g 'path/to/your/csvfile.csv'
```
Remember to replace `'topic'`, `'Your question here'`, and `'path/to/your/csvfile.csv'` with your actual topic, question, and CSV file path, respectively.

## Installation
Mac users please make sure that you have both Git and Python3 installed. Here are some basic instructions for installing these packages: https://chat.openai.com/share/4d44546d-7e67-435e-8b61-22c330ce7531
### Step 1: Clone the Repository Clone your repository to your local system.
In your terminal, run:
```sh
git clone https://github.com/CollOfTheWild/AskOpenAI.git
cd AskOpenAI
```
### Step 2: Create and Activate a Virtual Environment
Create a virtual environment in your project directory and activate it:
```sh
python3 -m venv askenv
source askenv/bin/activate
```
### Step 3: Install the OpenAI Python Package
You'll need to install the OpenAI Python package to interact with the API. You can install it using pip:
```sh
pip3 install openai
```
### Step 4: Add Your API Key
Before you can use the tool, you'll need to add your OpenAI API key to the script.
Provided that you have created an account with OpenAI and have connected a payment method for API usage, keys can be generated at https://platform.openai.com/account/api-keys

Once you have your key generated, export it to your virtual envorinment, please `your-api-key-here` with your actual API key:
```sh
export OPENAI_KEY=your-api-key-here
```
Replace `your-api-key-here` with your actual API key, save the file and exit the editor.

### Step 5: Run setup.sh
First, make the setup.sh script executable:
```sh
chmod +x setup.sh
```
Next, execute the setup.sh script. This script will automatically create a shebang line that points the script to the new virtual environment:
```sh
./setup.sh
```
This will ensure that the script uses the correct Python interpreter from the virtual environment where the OpenAI package is installed.
#### MAC USERS ONLY
On MacOS the path `/usr/local/bin` must be created before copying the script. This can be done using the following command:
```sh
sudo mkdir /usr/local/bin/ask
```
### Step 6: Move the Script to a System-wide Location
Move the script to a directory in the system's path, such as `/usr/local/bin` for Linux and Mac. Rename it to `ask` during the move:

```sh
sudo cp openai_cli.py /usr/local/bin/ask
```
### Step 7: Make the Script Executable Ensure the script is executable:
```sh
sudo chmod +x /usr/local/bin/ask
```
### Step 8: Deactivate the Virtual Environment
After completing the setup, you can deactivate the virtual environment:
```sh
deactivate
```
## Usage To use the tool, simply use the `ask` command followed by your query enclosed in single quotes:
```sh
ask 'Your question here'
```
The tool will then communicate with the OpenAI API and return the response directly in the terminal.
