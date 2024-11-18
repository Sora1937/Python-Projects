import speech_recognition as sr
import openai

# Initialize the recognizer
recognizer = sr.Recognizer()

# OpenAI API Key
openai.api_key = 'Insert Key Here'


# Here we are turning an Audio file into text using the Speech Recognition library
def transcribe_audio(audio_file):
    try:
        with sr.AudioFile(audio_file) as source:
            print("Listening to the audio...")
            audio_data = recognizer.record(source)
            # Convert Speech to rext
            text = recognizer.recognize_google(audio_data)
            print("Transcribed Text:", text)
            return text
    except Exception as e:
        print("Error:", e)
        return None



def send_to_chatgpt(prompt):
    try:
        response = openai.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': prompt}]
        )
        reply = response['choices'][0]['message']['content']
        return reply
    except Exception as e:
        print('Error communicating with ChatGPT:', e)
        return None
    
# Example of reading audio from a file
audio_file = "SelfProject/Audio/test.wav"

transcribed_text = transcribe_audio(audio_file)

if transcribed_text:
    print('Sending to ChatGPT...')
    chatgpt_response = send_to_chatgpt(transcribed_text)
    print('ChatGPT Response:', chatgpt_response)