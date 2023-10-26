#!/Users/coll/AskOpenAI/askenv/bin/python3

import openai
import sys
import csv
import os

openai.api_key = os.OPENAI_KEY

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

def main():
    if len(sys.argv) < 2:
        print("Usage: ask [-t topic] [-g csv_file_path] Your message here")
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

    # Check for the -g flag
    csv_data = None
    if '-g' in sys.argv:
        index = sys.argv.index('-g')
        if index < len(sys.argv) - 1:
            filepath = sys.argv[index + 1]
            csv_data = get_csv_data(filepath)
            if csv_data:
                csv_data_str = " ".join([", ".join(row) for row in csv_data])  # Convert CSV data to string
                filename = filepath.split('/')[-1]  # Get the file name from the file path
                user_message_content = (f"I have a dataset in a file named '{filename}'. Here is a sample of the data:"
                        f"{csv_data_str}"
                        f"I would like you to create a Python script that imports this CSV file (named '{filename}') and analyzes the data structure to select an appropriate visualization using the Seaborn library. "
                        f"Adhere to Edward Tufte's principles of data visualization, emphasizing clarity, precision, and efficiency. "
                        f"For categorical visualizations like bar charts, please use the 'hls' color palette; however, feel free to choose another palette that best suits other types of visualizations. "
                        f"Consider the distribution of numerical data, relationships between columns, and the presence of categorical data when selecting the visualization type. "
                        f"The script should save the visualization as a PNG file, be well-structured, and include comments explaining the choice of visualization, the selected color palette, and how the script works. "
                        f"It should also incorporate error handling for potential data inconsistencies. "
                        f"Note: Provide only the Python code without any additional commentary or instructions.")

                # Remove the -g flag and filepath from sys.argv
                del sys.argv[index:index+2]
            else:
                print("Error: Could not read data from CSV file")
                sys.exit(1)
        else:
            print("Error: No file path specified after -g")
            sys.exit(1)
    else:
        user_message_content = ' '.join(sys.argv[1:])

    # Setting messages outside of the flag blocks to prevent overwriting
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
