🗣️ Arabic Voice Assistant
A simple Arabic voice assistant that listens to your speech, understands your Arabic commands, and responds in spoken Arabic.

🔧 Built With
Whisper for Arabic speech-to-text

Cohere API for smart Arabic responses

gTTS for Arabic text-to-speech

pygame for audio playback

✅ Features
🎙️ Arabic voice input via your microphone

🧠 Smart Arabic responses powered by Cohere LLM

🔊 Arabic voice feedback using gTTS

🖥️ Lightweight, local processing (except for Cohere API)

📦 Requirements
Install the necessary dependencies:

bash
نسخ الكود
pip install speechrecognition pygame gtts openai-whisper cohere
Additional Requirement:
FFmpeg is required for Whisper to handle audio files.

On Windows:
Download and install from ffmpeg.org/download.html

On Linux/macOS:

bash
نسخ الكود
sudo apt install ffmpeg
🚀 How to Run
Clone this repository or copy the voice_assistant.py file.

Make sure your microphone is connected.

Run the script:

bash
نسخ الكود
python voice_assistant.py
You'll hear:

"أهلًا بك انا المساعد الصوتي الذكي! قل خروج لإنهاء المحادثة."

Then:

Speak in Arabic

It will:

Transcribe your voice with Whisper

Send the text to Cohere for response

Reply in Arabic using TTS

Say "خروج" or "إنهاء" to exit the loop.

🧠 Code Overview
1. Importing Libraries
python
نسخ الكود
import speech_recognition as sr
import cohere
import whisper
from gtts import gTTS
import pygame
import tempfile
import os
import time
2. API Setup
python
نسخ الكود
co = cohere.Client("YOUR_API_KEY")  # Replace with your actual API key securely
whisper_model = whisper.load_model("base")
💡 Never commit your API key to a public repository. Use environment variables or a config file instead.

3. speak(text) Function
Converts Arabic text to .mp3 using gTTS

Plays it back using pygame

4. record_audio()
Records audio input from your microphone using SpeechRecognition.

5. transcribe_with_whisper()
Uses Whisper to convert recorded Arabic speech into text.

6. get_reply(prompt)
Sends user input to Cohere API and returns the generated response.

7. main()
The main loop that:

Records voice

Transcribes it

Gets AI response

Speaks it back

💬 Example
نسخ الكود
🎙️ تفضل بالكلام...
👤 قلت: كيف حالك اليوم؟
🧠 المساعد: أنا بخير، شكرًا لسؤالك!
