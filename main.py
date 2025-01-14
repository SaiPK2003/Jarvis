import os
import base64
from openai import OpenAI
import streamlit as st

# Use an environment variable for the API key for better security practices.
client = OpenAI(api_key='***')

def get_answer(messages):
    system_message = [{"role": "system", "content": "You are a helpful AI chatbot, that answers questions asked by the User."}]
    messages = system_message + messages
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error during chat completion: {e}")
        return "An error occurred while processing your request."

def speech_to_text(audio_data):
    try:
        with open(audio_data, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                response_format="text",
                file=audio_file
            )
        return transcript
    except Exception as e:
        print(f"Error during speech-to-text: {e}")
        return "An error occurred while processing your audio."

def text_to_speech(input_text):
    try:
        response = client.audio.speech.create(
            model="tts-1",
            voice="nova",
            input=input_text
        )

        webm_file_path = "temp_audio.mp3"
        with open(webm_file_path, "wb") as f:
            with response.with_streaming_response() as stream:
                for chunk in stream.iter_bytes():
                    f.write(chunk)
        return webm_file_path
    except Exception as e:
        print(f"Error during text-to-speech: {e}")
        return "An error occurred while converting text to speech."

def autoplay_audio(file_path: str):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode("utf-8")
        md = f"""
        <audio autoplay>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        st.markdown(md, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error during audio playback: {e}")







