# 🧠 Offline Voice Chatbot using Python

An intelligent voice chatbot built entirely with **Python** that functions **offline**. It uses your **microphone** for voice input, converts it to text using the **Vosk speech recognition engine**, and responds through both **text and voice** using **pyttsx3**. Perfect for low-resource environments or privacy-focused applications.

---

## 📽️ Demo Video Script (Voice-over)

> Use this for your 1-minute demo video with your screen recording:

> 🎙️ Begin Voice Over:
Hi! This is my offline voice chatbot built using Python for the NSP Nexus Internship (Week 4).

This chatbot uses Vosk, an offline speech recognition engine, to convert voice into text. It also uses pyttsx3 for converting the chatbot's reply back to speech.

Let me quickly show you how it works.

markdown
Copy
Edit

> 🎙️ (Now run your Python file and start speaking to the chatbot live on screen. Wait for output.)

> Say a few phrases like:

- “Hello”
- “What is your name?”
- “Tell me a joke”
- “What time is it?”
- “Bye”

> 🎙️ End Voice Over:
And that’s it! The chatbot works completely offline, making it private, secure, and usable even without internet access.

Thank you!

yaml
Copy
Edit

---

## 🎯 Features

- 🎤 **Offline Voice Input** using Vosk
- 🔊 **Voice Output** using pyttsx3
- 💬 Real-time chatbot conversation
- 📅 Date and time queries
- 😂 Random jokes
- 🔐 Fully offline – No internet needed

---

## 📦 Technologies Used

| Tool        | Description                          |
|-------------|--------------------------------------|
| Python      | Programming Language                 |
| Vosk        | Offline Speech Recognition Engine    |
| pyttsx3     | Text-to-Speech Conversion (Offline)  |
| sounddevice | Audio Input from Microphone          |

---

## 📁 Project Structure

📦 offline-voice-chatbot/
┣ 📁 vosk-model/ # Pre-downloaded Vosk model folder
┣ 📜 offline_voice_chatbot.py # Main chatbot script
┣ 📜 requirements.txt # Required Python libraries
┗ 📜 README.md # Project documentation

yaml
Copy
Edit

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/offline-voice-chatbot
cd offline-voice-chatbot
2. Install Required Libraries
bash
Copy
Edit
pip install -r requirements.txt
Or manually install:

bash
Copy
Edit
pip install vosk pyttsx3 sounddevice
3. Download and Add Vosk Model
Visit: https://alphacephei.com/vosk/models

Download: vosk-model-small-en-us-0.15

Extract it and rename the folder to vosk-model

Place it inside the root directory (same folder as the Python file)

4. Run the Application
bash
Copy
Edit
python offline_voice_chatbot.py
💬 Example Commands to Try
“Hello”

“What is your name?”

“Tell me a joke”

“What time is it?”

“What is today’s date?”

“Bye”

🧪 Expected Output
vbnet
Copy
Edit
You: hello
Bot: Hello there! How can I help you today?

You: tell me a joke
Bot: Why don't scientists trust atoms? Because they make up everything!
