import streamlit as st
import json
import os
from dotenv import load_dotenv, set_key, dotenv_values

from app.backend.controller import process_user_input

# Define file path for storing chat data
CHAT_DATA_FILE = "data/JSON/chat_data.json"


def load_env():
    """
    Load environment variables from the .env file.

    Returns:
        dict: A dictionary of environment variables.
    """
    load_dotenv()
    return dotenv_values()


env_vars = load_env()


def init_chat_data():
    """
    Initialize the chat data file if it doesn't exist.
    """
    if not os.path.exists(CHAT_DATA_FILE):
        with open(CHAT_DATA_FILE, "w") as f:
            json.dump({}, f)


def store_message(user, role, content, audio_path=None):
    """
    Store a message in the chat data file.

    Args:
        user (str): The user's name.
        role (str): The role of the message sender (e.g., 'user' or 'assistant').
        content (str): The message content.
        audio_path (str, optional): The file path of the audio message.
    """
    with open(CHAT_DATA_FILE, "r") as f:
        try:
            chat_data = json.load(f)
        except json.JSONDecodeError:
            chat_data = {}

    if user not in chat_data:
        chat_data[user] = []

    message = {"role": role, "content": content}
    if audio_path:
        message["audio_path"] = audio_path

    chat_data[user].append(message)

    with open(CHAT_DATA_FILE, "w") as f:
        json.dump(chat_data, f, indent=4)


def get_messages(user):
    """
    Get messages for a specific user from the chat data file.

    Args:
        user (str): The user's name.

    Returns:
        list: A list of messages.
    """
    with open(CHAT_DATA_FILE, "r") as f:
        try:
            chat_data = json.load(f)
        except json.JSONDecodeError:
            chat_data = {}

    return chat_data.get(user, [])


def get_users():
    """
    Get a list of users from the chat data file.

    Returns:
        list: A list of user names.
    """
    with open(CHAT_DATA_FILE, "r") as f:
        try:
            chat_data = json.load(f)
            return list(chat_data.keys())
        except json.JSONDecodeError:
            return []


def save_to_env(variable, value):
    """
    Save a key-value pair to the .env file.

    Args:
        variable (str): The environment variable name.
        value (str): The environment variable value.
    """
    set_key('.env', variable, value)
    load_env()


# Initialize chat data file
init_chat_data()

# Set the page configuration
st.set_page_config(
    page_title="Sugar Bear (Deadpool)",
    page_icon="🤖",
    layout="wide",
)

# Title with GIF
col1, col2 = st.columns([3, 1])
with col1:
    st.title("Sugar Bear (Deadpool)")
    st.subheader("By Souradeep Banerjee")
    st.markdown('''
[![GitHub Stars](https://img.shields.io/github/stars/Souradeep1101/SugarBear.svg?style=social&label=Star&maxAge=2592000)](https://github.com/Souradeep1101/SugarBear/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/Souradeep1101/SugarBear.svg?style=social&label=Fork&maxAge=2592000)](https://github.com/Souradeep1101/SugarBear/network/members)[![YouTube Channel](https://img.shields.io/badge/YouTube-Channel-red.svg)](https://www.youtube.com/channel/UCv4ctQjbqZ0tq8lxchYkm2g)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Donate-yellow.svg)](https://www.buymeacoffee.com/souradeep1101)
    ''')
    st.link_button(label='GitHub', url='https://github.com/Souradeep1101/')

with col2:
    st.image('images/deadpool-dance-bye-bye-bye.gif', use_column_width=True)
# Authentication menu in the sidebar
st.divider()
st.sidebar.header("Authentication Settings")

with st.sidebar.form(key='auth_form'):
    elevenlabs_api_key = st.text_input("ElevenLabs API Key", value=env_vars.get("ELEVENLABS_API_KEY", ""),
                                       type="password")
    custom_voice_id = st.text_input("Custom Voice ID", value=env_vars.get("CUSTOM_VOICE_ID", ""), type="password")
    openai_api_key = st.text_input("OpenAI API Key", value=env_vars.get("OPENAI_API_KEY", ""), type="password")
    langflow_store_env = st.text_input("LangFlow Store Environment Variables",
                                       value=env_vars.get("LANGFLOW_STORE_ENVIRONMENT_VARIABLES", ""), type="password")
    astra_db_api_endpoint = st.text_input("Astra DB API Endpoint", value=env_vars.get("ASTRA_DB_API_ENDPOINT", ""),
                                          type="password")
    astra_db_application_token = st.text_input("Astra DB Application Token",
                                               value=env_vars.get("ASTRA_DB_APPLICATION_TOKEN", ""), type="password")
    submit_button = st.form_submit_button(label='Save')

if submit_button:
    save_to_env("ELEVENLABS_API_KEY", elevenlabs_api_key)
    save_to_env("CUSTOM_VOICE_ID", custom_voice_id)
    save_to_env("OPENAI_API_KEY", openai_api_key)
    save_to_env("LANGFLOW_STORE_ENVIRONMENT_VARIABLES", langflow_store_env)
    save_to_env("ASTRA_DB_API_ENDPOINT", astra_db_api_endpoint)
    save_to_env("ASTRA_DB_APPLICATION_TOKEN", astra_db_application_token)
    st.sidebar.success("Authentication settings saved successfully!")
    env_vars = load_env()

# Check if all required environment variables are set
required_keys = [
    "ELEVENLABS_API_KEY", "CUSTOM_VOICE_ID", "OPENAI_API_KEY",
    "LANGFLOW_STORE_ENVIRONMENT_VARIABLES", "ASTRA_DB_API_ENDPOINT", "ASTRA_DB_APPLICATION_TOKEN"
]

all_keys_provided = all(env_vars.get(key) for key in required_keys)

if not all_keys_provided:
    st.error("Please provide all authentication settings in the sidebar to use the app.")
else:
    # User name input with form
    st.sidebar.header("User Settings")
    with st.sidebar.form(key='username_form'):
        users = get_users()
        selected_user = st.selectbox("Select existing user", options=users)
        user_name = st.text_input("Or enter a new unique name", value="", placeholder="User")
        submit_button = st.form_submit_button(label='Confirm Username')

    if submit_button:
        if user_name:
            selected_user = user_name
        if selected_user:
            st.sidebar.success(f"Welcome, {selected_user}!")

            # Initialize session state for storing chat history
            st.session_state.user_name = selected_user
            messages = get_messages(selected_user)
            if messages:
                st.session_state.messages = messages
            else:
                st.session_state.messages = []
                st.sidebar.warning(f"No chat history found for {selected_user}. Starting a new session.")
        else:
            st.sidebar.error("Please select or enter a unique name.")

    # Display chat history
    if "messages" in st.session_state:
        for message in st.session_state.messages:
            role, content = message["role"], message["content"]
            with st.chat_message(role):
                st.markdown(content)
                if "audio_path" in message:
                    with open(message["audio_path"], "rb") as audio_file:
                        audio_bytes = audio_file.read()
                    st.audio(audio_bytes, format="audio/mp3", autoplay=False)

    # User input
    if "user_name" in st.session_state and (prompt := st.chat_input("What is up?")):
        if not all(env_vars.get(key) for key in required_keys):
            st.error("One or more authentication keys are missing. Please update them in the sidebar.")
        else:
            st.session_state.messages.append({"role": "user", "content": prompt})
            store_message(st.session_state.user_name, "user", prompt)
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                with st.spinner("Generating response..."):
                    response_text, audio_file_path = process_user_input(prompt, st.session_state.user_name)
                    st.markdown(response_text)
                st.session_state.messages.append(
                    {"role": "assistant", "content": response_text, "audio_path": audio_file_path})
                store_message(st.session_state.user_name, "assistant", response_text, audio_file_path)

                # Autoplay audio only the first time it is generated
                if audio_file_path:
                    try:
                        with open(audio_file_path, "rb") as audio_file:
                            audio_bytes = audio_file.read()
                        st.audio(audio_bytes, format="audio/mp3", autoplay=True)
                    except Exception as e:
                        st.error(f"Error loading audio: {str(e)}")
