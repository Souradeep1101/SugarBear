# app/backend/services/elevenlabs_service.py

import os
import uuid
from typing import IO
from io import BytesIO
from dotenv import load_dotenv
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

# Load environment variables from the .env file
load_dotenv()

# Retrieve ElevenLabs API key and custom voice ID from environment variables
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
CUSTOM_VOICE_ID = os.getenv("CUSTOM_VOICE_ID")

# Initialize the ElevenLabs client with the API key
client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)


def text_to_speech_file(text: str) -> str:
    """
    Convert the provided text to speech and save it as an MP3 file.

    This function uses the ElevenLabs API to convert the input text to speech,
    saves the resulting audio as an MP3 file, and returns the file path.

    Args:
        text (str): The input text to be converted to speech.

    Returns:
        str: The file path of the saved MP3 file.
    """
    # Calling the text-to-speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id=CUSTOM_VOICE_ID,
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_multilingual_v2",
        voice_settings=VoiceSettings(
            stability=1.0,
            similarity_boost=1.0,
            style=0.34,
            use_speaker_boost=True,
        ),
    )

    # Generating a unique file name for the output MP3 file
    save_file_path = f"data/audio/{uuid.uuid4()}.mp3"

    # Writing the audio to a file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: A new audio file was saved successfully!")

    # Return the path of the saved audio file
    return save_file_path


def text_to_speech_stream(text: str) -> IO[bytes]:
    """
    Convert the provided text to speech and return the audio as a stream.

    This function uses the ElevenLabs API to convert the input text to speech
    and returns the resulting audio data as a BytesIO stream.

    Args:
        text (str): The input text to be converted to speech.

    Returns:
        IO[bytes]: A BytesIO stream containing the audio data.
    """
    # Perform the text-to-speech conversion
    response = client.text_to_speech.convert(
        voice_id=CUSTOM_VOICE_ID,
        output_format="mp3_44100_128",
        text=text,
        model_id="eleven_multilingual_v2",
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    # Create a BytesIO object to hold the audio data in memory
    audio_stream = BytesIO()

    # Write each chunk of audio data to the stream
    for chunk in response:
        if chunk:
            audio_stream.write(chunk)

    # Reset stream position to the beginning
    audio_stream.seek(0)

    # Return the stream for further use
    return audio_stream
