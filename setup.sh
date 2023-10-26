#!/bin/bash

# Get the full path of the current directory
DIR="$(pwd)"

# Construct the shebang line
SHEBANG="#!$DIR/askenv/bin/python3"

# Add the shebang line to the beginning of the openai_cli.py file
echo -e "$SHEBANG\n$(cat openai_cli.py)" > openai_cli.py
