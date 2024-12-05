import getpass
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# List to keep track of manually added variables
manually_added_vars = {}
tokens_needed = ["HUGGINGFACEHUB_API_TOKEN"]

# Check if each token in tokens_needed is set
for token_name in tokens_needed:
    if not os.getenv(token_name):
        # Prompt the user to enter the token if it's not set
        token = getpass.getpass(f"Enter your {token_name}: ")
        os.environ[token_name] = token
        manually_added_vars[token_name] = token

# Write only manually added variables to a .env file so that they can be used in the future automatically
with open(".env", "w") as env_file:
    for var, value in manually_added_vars.items():
        env_file.write(f"{var}={value}\n")