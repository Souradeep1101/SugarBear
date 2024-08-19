# app/backend/controller.py

from app.backend.services.elevenlabs_service import text_to_speech_file
from app.backend.services.langflow_service import get_response_from_api


def process_user_input(user_input: str, user: str = '') -> tuple:
    """
    Process the user's input by generating a response text and converting it to speech.

    This function takes the user's input, generates a response using the LangFlow service,
    and converts the response text to an audio file using the ElevenLabs service.

    Args:
        user_input (str): The input text provided by the user.
        user (str): The name of the user (optional).

    Returns:
        tuple: A tuple containing the response text and the path to the generated audio file.
    """
    # Generate response text using LangFlow service
    response_text = get_response_from_api(user_input, user)

    # Convert the response text to an audio file using ElevenLabs service
    audio_file = text_to_speech_file(response_text)

    # Return the response text and the path to the generated audio file
    return response_text, audio_file
