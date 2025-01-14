# JARVIS AI Assistant

## Introduction  
**JARVIS AI Assistant** is a prototype software designed to replicate the functionality of Tony Stark’s JARVIS from *Iron Man*. The aim is to achieve seamless, real-time communication with an AI assistant using custom earphones or microphones. It supports voice-based interactions, providing text-to-speech (TTS) and speech-to-text (STT) functionalities, along with dynamic chat-based responses powered by OpenAI's GPT-3.5-turbo.  

This project brings the concept of an intelligent, always-available assistant closer to reality by combining AI-driven natural language processing with a user-friendly interface.

---

## Features  
1. **Real-Time Voice Communication**:  
   - Users can record audio directly using a microphone or earphone.
   - Audio is transcribed into text using OpenAI's Whisper model.

2. **Dynamic Chat Responses**:  
   - The transcribed text is processed to generate a natural and conversational response using GPT-3.5-turbo.  
   - Supports context-based conversations with session state management.

3. **Text-to-Speech Conversion**:  
   - Converts AI responses into audio files using TTS.
   - Automatically plays the generated audio to simulate real-time conversation.

4. **Interactive UI**:  
   - Built with **Streamlit** for an intuitive and minimalist user experience.
   - Chat-style interface displays user and assistant messages interactively.

5. **Customizable**:  
   - Can be adapted for use on various platforms, integrating with different hardware solutions for a seamless "always-on" assistant experience.

---

## Installation  

### Prerequisites
- Python 3.8+
- OpenAI API key  
- Libraries:  
  - `streamlit`  
  - `audio_recorder_streamlit`  
  - `streamlit_float`  
  - `openai`
