import os
import requests
from dotenv import load_dotenv
from typing import Optional

from langflow.load import run_flow_from_json

# Load environment variables from the .env file
load_dotenv()

# Retrieve API key and other environment variables
api_key = os.getenv("OPENAI_API_KEY")
endpoint = os.getenv("ASTRA_DB_API_ENDPOINT")
token = os.getenv("ASTRA_DB_APPLICATION_TOKEN")

# Constants
BASE_API_URL = "http://127.0.0.1:7860"
FLOW_ID = "5ef1758d-2fba-4e18-a81e-55655fe0d1c6"


def get_tweaks(user: str, text: str):
    return {
        # "AstraVectorStoreComponent-iDq1f": {
        #     "api_endpoint": endpoint,
        #     "collection_name": "sugarbear",
        #     "token": token
        # },
        # "OpenAIEmbeddings-YCeF1": {
        #     "openai_api_key": api_key
        # },
        # "OpenAIEmbeddings-JBSgu": {
        #     "openai_api_key": api_key
        # },
        # "OpenAIModel-ApXpI": {
        #     "api_key": api_key,
        #     "model_name": "gpt-4"
        # }
        "TextInput-xq3Cn": {
            "input_value": user
        },
        "ChatInput-nYnEh": {
            "input_value": text,
        },
    }


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
    TWEAKS = get_tweaks(user, text)
    TWEAKS["TextInput-xq3Cn"]["input_value"] = user

    response = run_flow_from_json(
        flow="data/JSON/Sugar Bear (Deadpool).json",
        input_value=text,
        tweaks=TWEAKS,
    )

    return str(response[0].outputs[0].messages[0].message)


def run_flow_from_api(message: str, tweaks: Optional[dict] = None) -> dict:
    """
    Run a flow with a given message and optional tweaks using a curl command.

    :param message: The message to send to the flow
    :param tweaks: Optional tweaks to customize the flow
    :return: The JSON response from the flow
    """
    api_url = f"{BASE_API_URL}/api/v1/run/{FLOW_ID}"
    payload = {
        # "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    if tweaks:
        payload["tweaks"] = tweaks
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(api_url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")


def get_response_from_api(text, user):
    """
        Generate a response based on the user's input text using LangFlow.

        This function takes the user's input text and an optional user identifier,
        applies tweaks to the LangFlow configuration, and runs the LangFlow JSON
        workflow to generate a response.

        Args:
            text (str): The input text provided by the user.
            user (str): The name of the user.

        Returns:
            str: The generated response text.
        """
    tweaks = get_tweaks(user, text)
    message = text
    response = run_flow_from_api(message, tweaks)
    # print(json.dumps(response, indent=2))
    return str(response['outputs'][0]['outputs'][0]['results']['message']['data']['text'])

# run_flow('Who are you?', 'Ryan Reynolds the Great')
