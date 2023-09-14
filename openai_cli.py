

import openai
import sys
import csv

openai.api_key = "your-openai-api-key-here"

# Function to get the data from the beginning of the CSV file
def get_csv_data(filepath):
    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = [next(reader, None)]  # Get the header
        for i in range(20):  # Get the first 20 rows of data (adjust as necessary)
            row = next(reader, None)
            if row:
                data.append(row)
        return data

# Function to get the message from the command line arguments
def get_message():
    if '-g' in sys.argv:
        index = sys.argv.index('-g')
        if index < len(sys.argv) - 1:
            filepath = sys.argv[index + 1]
            csv_data = get_csv_data(filepath)
            if csv_data:
                return " ".join(sys.argv[1:index]), csv_data, filepath
            else:
                print("Error: Could not read data from CSV file")
                sys.exit(1)
        else:
            print("Error: No file path specified after -g")
            sys.exit(1)
    else:
        return " ".join(sys.argv[1:]), None, None

# Get the message and csv data from the command line arguments
message, csv_data, filepath = get_message()

# Construct the messages parameter for the API call
if csv_data:
    csv_data_str = "\n".join([", ".join(row) for row in csv_data])  # Convert CSV data to string
    filename = filepath.split('/')[-1]  # Get the file name from the file path
    message = (f"I have a dataset in a file named '{filename}'. Here is an example of what the data looks like, as shown below:\n\n"
               f"{csv_data_str}\n\n"
               f"I want you to create a Python script to import this CSV file (named '{filename}') and visualize this data using Seaborn, and then save a PNG of the visualization. Don't include any commentary or instructions, only the Python code. Do not include a code block or backticks.")
    messages = [
        {"role": "system", "content": "You are a helpful assistant that writes Python scripts for data visualization."},
        {"role": "user", "content": message}
    ]
else:
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": message}
    ]

# Communicate with the OpenAI API
completion = openai.ChatCompletion.create(
  model="gpt-4-0613",
  messages=messages
)

# Print the response message
print(completion.choices[0].message['content'])
