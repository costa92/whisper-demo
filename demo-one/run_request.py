import os
import requests
from openai import OpenAI

def get_env_variable(var_name, default_value=""):
    """Retrieve environment variable or return default."""
    return os.getenv(var_name, default_value)

def initialize_openai_client(api_key, api_base):
    """Initialize the OpenAI client."""
    if not api_key or not api_base:
        raise ValueError("Please ensure 'DEERAPI_KEY' and 'DEERAPI_URL' environment variables are set.")
    return OpenAI(api_key=api_key, base_url=api_base)

def download_audio_file(url, local_path):
    """Download an audio file from a URL to a local path."""
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    with open(local_path, 'wb') as file:
        file.write(response.content)

def transcribe_audio(client, audio_path, model_name="whisper-1"):
    """Transcribe audio using the OpenAI client."""
    with open(audio_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(model=model_name, file=audio_file)
    return transcription.text

def main():
    api_key = get_env_variable("DEERAPI_KEY")
    api_base = get_env_variable("DEERAPI_URL")
    client = initialize_openai_client(api_key, api_base)

    audio_url = "https://livehub-cdn.hellotalk8.com/recording/vr/7881e53fdb4e92eff1db369da007cf2d_VR_143600924_1738813283953152844_0.mp3"
    audio_path = "7881e53fdb4e92eff1db369da007cf2d_VR_143600924_1738813283953152844_0.mp3"
    download_audio_file(audio_url, audio_path)

    transcription_text = transcribe_audio(client, audio_path)
    print(transcription_text)

if __name__ == "__main__":
    main()