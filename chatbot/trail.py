from vosk import Model, KaldiRecognizer
import pyttsx3
import sounddevice as sd
import queue
import json
import os
import datetime
import random
import time

def speak(text):
    print("Bot:", text)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()

model_path = "vosk-model"
if not os.path.exists(model_path):
    print(" Vosk model not found! Please download and extract to 'vosk-model'")
    exit()

model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print("Mic error:", status)
    q.put(bytes(indata))

def get_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hi", "hello", "hey"]:
        return "Hey there! How can I help you?"

    elif "how are you" in user_input:
        return "I'm doing great, thanks for asking!"

    elif "your name" in user_input:
        return "I'm your offline chatbot built just for you."

    elif "joke" in user_input:
        jokes = [
            "Why did the computer get cold? Because it left its Windows open!",
            "Why don’t skeletons fight each other? They don’t have the guts.",
            "What do you call fake spaghetti? An impasta!"
        ]
        return random.choice(jokes)

    elif "time" in user_input:
        return "The current time is " + datetime.datetime.now().strftime("%I:%M %p")

    elif "date" in user_input:
        return "Today is " + datetime.datetime.now().strftime("%A, %B %d, %Y")

    elif "thank" in user_input:
        return "You're welcome! Let me know if you need anything else."

    elif user_input in ["bye", "exit", "quit", "goodbye"]:
        return "Goodbye! Talk to you later."

    elif user_input.strip() == "":
        return "Hmm, I didn't catch that. Please try again."

    else:
        return "I'm still learning. Try asking about the time, date, or a joke!"

# ---------------------- Welcome -----------------------
speak("Hello! I'm your offline chatbot. You can talk to me now.")

# ---------------------- Main Chat Loop ----------------------
while True:
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("🎤 Listening... Speak now (pause to finish)")
        recognizer = KaldiRecognizer(model, 16000)
        result_text = ""
        silence_timeout = 3  # seconds of silence to detect end of speech
        silence_start = time.time()

        while True:
            data = q.get()

            if recognizer.AcceptWaveform(data):
                result_json = recognizer.Result()
                partial = json.loads(result_json).get("text", "")
                if partial:
                    result_text += " " + partial
                    silence_start = time.time()  # reset timer

            # Stop if silence for 3+ seconds
            if time.time() - silence_start > silence_timeout:
                break

        user_input = result_text.strip()
        print("You:", user_input)

        reply = get_response(user_input)
        speak(reply)

        if "goodbye" in reply.lower():
            break
