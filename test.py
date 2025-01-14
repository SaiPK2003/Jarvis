# from openai import OpenAI
# client = OpenAI(api_key='')

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message)

# Python program to translate
# speech to text and text to speech

# import openai
# import os
# import assemblyai as aai 
# import elevenlabs
# from queue import Queue

# #client = OpenAI(api_key=os.environ.get(""))
# # openai.api_key = ''

# # # #Set API Keys
# openai.api_key = ''
# aai.settings.api_key = ""
# elevenlabs.set_api_key("")

# transcript_queue = Queue()


# def on_data(transcript: aai.RealtimeTranscript):
#     if not transcript.text:
#         return
#     if isinstance(transcript, aai.RealtimeFinalTranscript):
#         transcript_queue.put(transcript.text + '')
#         print("User:", transcript.text, end="\r\n")
#     else:
#         print(transcript.text, end="\r")

# def on_error(error: aai.RealtimeError):
#     print("An error occured:", error)

# # Conversation loop
# def handle_conversation():
#     while True:
#         transcriber = aai.RealtimeTranscriber(
#             on_data=on_data,
#             on_error=on_error,
#             sample_rate=44_100,
#         )

#         # Start the connection
#         transcriber.connect()

#         # Open  the microphone stream
#         microphone_stream = aai.extras.MicrophoneStream()

#         # Stream audio from the microphone
#         transcriber.stream(microphone_stream)

#         # Close current transcription session with Ctrl + C
#         transcriber.close()

#         # Retrieve data from queue
#         transcript_result = transcript_queue.get()

#         user_input = "What is the capital of France?"

#         MODEL = "gpt-3.5-turbo"
#         #response = client.chat.completions.create(
#         response = openai.chat.completions.create(
#             model=MODEL,
#             messages=[
#                 {"role": "system", "content": "Assume your name is Jarvis and you are a highly skilled, helpful assistant that answers questions."},
#                 {"role": "user", "content": transcript_result},
#             ],
#             temperature=0,
#         )

#         text = response.choices[0].message.content

#         # Convert the response to audio and play it
#         audio = elevenlabs.generate(
#             text=text,
#             voice="Adam" # or any voice of your choice
#         )

#         print("\nAI:", text, end="\r\n")

#         elevenlabs.play(audio)

# handle_conversation()


# import elevenlabs

# elevenlabs.set_api_key("")

# audio = elevenlabs.generate(
#     text = "Testing 1, 2, 3",
#     voice = "Adam"
# )

# elevenlabs.play(audio)



# user_input = "What is the capital of France?"
# print("USER:", user_input)

# # Send the user input to OpenAI for response generation
# response = openai.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a highly skilled, helpful assistant that answers questions."},
#         {"role": "user", "content": user_input}
#     ],
#     temperature=0
# )

# # Get the AI response from OpenAI
# ai_response = response.choices[0].message.content
# print("AI:", ai_response)

# # Convert the AI response to audio using Eleven Labs API
# audio = elevenlabs.generate(
#     text=ai_response,
#     voice="Adam"  # Replace with the voice you want to use
# )

# # Play the audio
# elevenlabs.play(audio)

import openai
import os
import assemblyai as aai 
import elevenlabs
from queue import Queue
import time

openai.api_key = '**'
aai.settings.api_key = "**"
elevenlabs.set_api_key("**")

transcript_queue = Queue()
last_transcript_time = 0

def on_data(transcript: aai.RealtimeTranscript):
    global last_transcript_time

    if not transcript.text:
        return

    if isinstance(transcript, aai.RealtimeFinalTranscript):
        transcript_queue.put(transcript.text + '')
        print("User:", transcript.text)

        # Calculate the time difference since the last transcript
        time_diff = time.time() - last_transcript_time
        last_transcript_time = time.time()

        # If there's a pause in speech, trigger GPT response
        if time_diff > 1.5:  # Adjust the threshold as needed
            trigger_gpt_response()
    else:
        print(transcript.text, end="")

def trigger_gpt_response():
    if not transcript_queue.empty():
        transcript_result = transcript_queue.get()
        user_input = transcript_result.strip()

        MODEL = "gpt-3.5-turbo"
        response = openai.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "Assume your name is Jarvis and you are a highly skilled, helpful assistant that answers questions."},
                {"role": "user", "content": user_input},
            ],
            temperature=0,
        )

        text = response.choices[0].message.content

        audio = elevenlabs.generate(
            text=text,
            voice="Adam"
        )

        print("AI:", text)
        elevenlabs.play(audio)

def on_error(error: aai.RealtimeError):
    print("An error occurred:", error)

def handle_conversation():
    while True:
        transcriber = aai.RealtimeTranscriber(
            on_data=on_data,
            on_error=on_error,
            sample_rate=44_100,
        )

        transcriber.connect()

        microphone_stream = aai.extras.MicrophoneStream()

        transcriber.stream(microphone_stream)

        transcriber.close()

handle_conversation()






