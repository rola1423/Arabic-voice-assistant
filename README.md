# 🗣️ Arabic Voice Assistant

This is a simple **Arabic voice assistant** that listens to your voice, understands your Arabic commands, and responds with spoken Arabic.

Built using:
- [Whisper](https://github.com/openai/whisper) for Arabic speech-to-text
- [Cohere](https://cohere.com/) API for smart responses
- [gTTS](https://pypi.org/project/gTTS/) for Arabic text-to-speech
- [pygame](https://www.pygame.org/) to play the generated audio

---

## ✅ Features

- 🎙️ Arabic voice input using your microphone
- 🧠 Smart Arabic replies powered by Cohere's LLM
- 🗣️ Arabic text-to-speech via gTTS
- 🔊 Audio response playback using pygame
- 🖥️ Fully runs locally (except Cohere API)

---

## 📦 Requirements

Install dependencies using:

```bash
pip install speechrecognition pygame gtts openai-whisper cohere
You also need ffmpeg for Whisper to process audio files.

On Windows: install from https://ffmpeg.org/download.html

On Linux/macOS:

```bash

sudo apt install ffmpeg
🚀 How to Run
Clone this repo or copy the voice_assistant.py file.

Make sure your microphone is connected.

Run the script:

```bash

python voice_assistant.py
You will hear:

"أهلًا بك انا المساعد الصوتي الذكي! قل خروج لإنهاء المحادثة."

Then:

Speak in Arabic.

It transcribes your speech using Whisper.

Sends the transcribed text to Cohere for response.

Replies back to you in Arabic using TTS audio.

Say "خروج" or "إنهاء" to exit.

🧠 Code Structure & Explanation
1. Library Imports
python

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
co = cohere.Client("YOUR_API_KEY")
whisper_model = whisper.load_model("base")
3. Speak Function
python

def speak(text):
    ...
Converts Arabic text to .mp3 using gTTS.

Plays the result with pygame.

4. Record Audio
python

def record_audio(filename="temp.wav"):
    ...
Records from your microphone using speech_recognition.

5. Transcribe Audio
python

def transcribe_with_whisper(filename):
    ...
Uses Whisper model to convert Arabic voice to text.

6. Get AI Response
pytho

def get_reply(prompt):
    ...
Sends user text to Cohere API and returns the response.

7. Main Loop
python

def main():
    ...
Repeats the full loop:

Record

Transcribe

Get AI reply

Speak it back

💬 Example Output

🎙️ تفضل بالكلام...
👤 قلت: كيف حالك اليوم؟
