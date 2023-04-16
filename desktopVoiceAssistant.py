from gtts import gTTS
import openai
import os
import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()

# use the microphone as the source of input
with sr.Microphone() as source:
    print("Say something!")
    # listen for audio and store it in audio_data variable
    audio_data = r.record(source, duration=8)

    # recognize speech using Google Speech Recognition
    text = r.recognize_google(audio_data)

    # print the recognized text
    print("You said:", text)


openai.api_key = "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"

# Define the prompt you want to generate text from
prompt = text

# Set the parameters for the text generation
model = "text-davinci-003"
temperature = 0.7
max_tokens = 100

# Generate the text
response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens,
)

# Print the generated text


# specify the text you want to convert to audio
newtext = response.choices[0].text

# create a gTTS object and set language to English (en)
tts = gTTS(text=newtext, lang='en')

# save the audio file
tts.save("test.mp3")

# play the audio file
os.system("test.mp3")  # replace 'mpg321' with your audio player command

print(response.choices[0].text)
