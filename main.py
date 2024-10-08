import subprocess
import sys


def main():
    print('''
▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
▐   ▄████████ ███    █▄     ▄██████▄     ▄████████    ▄████████▌
▐  ███    ███ ███    ███   ███    ███   ███    ███   ███    ███▌
▐  ███    █▀  ███    ███   ███    █▀    ███    ███   ███    ███▌
▐  ███        ███    ███  ▄███          ███    ███  ▄███▄▄▄▄██▀▌
▐▀███████████ ███    ███ ▀▀███ ████▄  ▀███████████ ▀▀███▀▀▀▀▀  ▌
▐         ███ ███    ███   ███    ███   ███    ███ ▀███████████▌
▐   ▄█    ███ ███    ███   ███    ███   ███    ███   ███    ███▌
▐ ▄████████▀  ████████▀    ████████▀    ███    █▀    ███    ███▌
▐                                                    ███    ███▌
▐▀█████████▄     ▄████████    ▄████████    ▄████████           ▌
▐  ███    ███   ███    ███   ███    ███   ███    ███           ▌
▐  ███    ███   ███    █▀    ███    ███   ███    ███           ▌
▐ ▄███▄▄▄██▀   ▄███▄▄▄       ███    ███  ▄███▄▄▄▄██▀           ▌
▐▀▀███▀▀▀██▄  ▀▀███▀▀▀     ▀███████████ ▀▀███▀▀▀▀▀             ▌
▐  ███    ██▄   ███    █▄    ███    ███ ▀███████████           ▌
▐  ███    ███   ███    ███   ███    ███   ███    ███           ▌
▐▄█████████▀    ██████████   ███    █▀    ███    ███           ▌
▐                                         ███    ███           ▌
▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
    ''')
    print('By Souradeep Banerjee')
    # Start the streamlit app
    subprocess.run([sys.executable, "-m", "streamlit", "run", "app/frontend/streamlit_app.py"])


if __name__ == "__main__":
    main()
