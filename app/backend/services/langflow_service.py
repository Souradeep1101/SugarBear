from langflow.load import run_flow_from_json
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve API key and other environment variables
api_key = os.getenv("OPENAI_API_KEY")
endpoint = os.getenv("ASTRA_DB_API_ENDPOINT")
token = os.getenv("ASTRA_DB_APPLICATION_TOKEN")


def get_response(text, user=""):
    """
    Generate a response based on the user's input text using LangFlow.

    This function takes the user's input text and an optional user identifier,
    applies tweaks to the LangFlow configuration, and runs the LangFlow JSON
    workflow to generate a response.

    Args:
        text (str): The input text provided by the user.
        user (str): The name of the user (optional).

    Returns:
        str: The generated response text.
    """
    # Define tweaks for the LangFlow configuration
    TWEAKS = {
        "TextInput-xq3Cn": {
            "input_value": user
        },
    }

    # Run the LangFlow JSON workflow with the provided input text and tweaks
    response = run_flow_from_json(
        flow=r"data\JSON\Sugar Bear (Deadpool).json",
        input_value=text,
        tweaks=TWEAKS,
    )

    # Return the generated response text
    return str(response[0].outputs[0].messages[0].message)
