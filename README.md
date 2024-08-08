# Sugar Bear (Deadpool)

---
[![GitHub Stars](https://img.shields.io/github/stars/Souradeep1101/SugarBear.svg?style=social&label=Star&maxAge=2592000)](https://github.com/Souradeep1101/LibraryManagementSystem/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/Souradeep1101/SugarBear.svg?style=social&label=Fork&maxAge=2592000)](https://github.com/Souradeep1101/LibraryManagementSystem/network/members)
[![YouTube Channel](https://img.shields.io/badge/YouTube-Channel-red.svg)](https://www.youtube.com/channel/UCv4ctQjbqZ0tq8lxchYkm2g)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Donate-yellow.svg)](https://www.buymeacoffee.com/souradeep1101)
<img src="images/deadpool_heart_love.gif" alt="Deadpool Heart Love" width="30" height="30">

![Deadpool Dancing](images/deadpool-dance-bye-bye-bye-bye.gif)

Welcome to the Sugar Bear-Deadpool Chatbot. A project involved in creating a unique, smart, and a little bit
sarcastic Deadpool character for engaging, interesting talk. Made with good humor and compatibility with Streamlit,
ElevenLabs, and LangFlow, this chatbot is sure to make these interactions unforgettable.

## 📌 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
    - [Prerequisites](#prerequisites)
    - [Clone the Repository](#clone-the-repository)
    - [Set Up the Environment](#set-up-the-environment)
- [Directory Structure](#-directory-structure)
- [Usage](#-usage)
- [Legal and Ethical Considerations](#-legal-and-ethical-considerations)
- [Acknowledgements](#-acknowledgements)
- [License](#-license)
- [Contact](#-contact)

## ✨ Features

- **Conversational AI**: Engage in dynamic conversations with Deadpool.
- **Text-to-Speech**: Hear responses in Deadpool's voice using ElevenLabs.
- **User Authentication**: Secure your app with API keys and environment variables.
- **Chat History**: Store and retrieve chat histories for individual users.
- **Interactive UI**: Enjoy a user-friendly interface built with Streamlit.

## ⚙️ Installation

### Prerequisites

- Python 3.10 or higher
- [Streamlit](https://streamlit.io/)
- [ElevenLabs](https://elevenlabs.io/)
- [LangFlow](https://langflow.io/)

### Clone the Repository

```bash
git clone https://github.com/Souradeep1101/SugarBear
cd SugarBear
```

### Set Up the Environment

1. **Create a virtual environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables**

   Create a `.env` file in the root directory and add the following variables:

    ```bash
    ELEVENLABS_API_KEY=<your-elevenlabs-api-key>
    CUSTOM_VOICE_ID=<your-custom-voice-id>
    OPENAI_API_KEY=<your-openai-api-key>
    LANGFLOW_STORE_ENVIRONMENT_VARIABLES=<your-langflow-store-env>
    ASTRA_DB_API_ENDPOINT=<your-astra-db-api-endpoint>
    ASTRA_DB_APPLICATION_TOKEN=<your-astra-db-application-token>
    ```

## 🏗️ Directory Structure

```plaintext
SugarBear/
├── app/
│   ├── frontend/
│   │   └── streamlit_app.py
│   ├── backend/
│   │   ├── controller.py
│   │   └── services/
│   │       ├── langflow_service.py
│   │       └── elevenlabs_service.py
├── data/
│   ├── audio/
│   │   └── [audio files]
│   ├── JSON/
│       ├── chat_data.json
│       └── Sugar Bear (Deadpool).json
├── images/
│   ├── deadpool-dance-bye-bye-bye.gif
│   ├── deadpool-dance-bye-bye-bye-bye.gif
│   └── deadpool_heart_love.gif
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

## 🚀 Usage

1. **Run the application**

    ```bash
    python main.py
    ```

2. **Access the Streamlit app**

   Open your browser and go to `http://localhost:8501`.

3. **Authenticate**

   Enter the required API keys and environment variables in the sidebar and save them.

4. **Start Chatting**

    - Select an existing user or create a new one.
    - Type your message in the chat input box.
    - The chatbot will respond in Deadpool's style, and the response will be converted to audio.

## ⚖️ Legal and Ethical Considerations

By using this project, you agree to the following:

1. You have read and agree to comply with
   ElevenLabs' [Terms of Service](https://elevenlabs.io/terms-of-use), [Privacy Policy](https://elevenlabs.io/privacy-policy),
   and [Prohibited Content and Uses Policy](https://elevenlabs.io/use-policy).
2. You will not use this project for any illegal, fraudulent, or harmful purpose.
3. You will provide proper attribution to ElevenLabs if you are using a free plan.
4. This project is for personal and educational use only and is not intended for commercial purposes.
5. You have the necessary rights or permissions to use any voice samples uploaded to ElevenLabs for cloning.

## 🙌 Acknowledgements

- [**ElevenLabs**](https://elevenlabs.io) for providing the voice cloning technology.
- [**Ryan Reynolds and Marvel**](https://www.marvel.com) for the Deadpool character.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

For any questions or issues, please contact me through [Email](mailto:rishibanerjee1101@gmail.com).
