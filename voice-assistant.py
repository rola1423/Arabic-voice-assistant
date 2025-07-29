import speech_recognition as sr
import cohere
import whisper
from gtts import gTTS
import pygame
import tempfile
import os
import time

# إعداد Cohere
co = cohere.Client("YOUR_API_KEY")  # Replace with your actual key in local use

# تحميل نموذج Whisper 
whisper_model = whisper.load_model("base")

# دالة لتحويل النص إلى صوت
def speak(text):
    fd, path = tempfile.mkstemp(suffix=".mp3")
    os.close(fd)
    try:
        tts = gTTS(text=text, lang='ar')
        tts.save(path)
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        pygame.mixer.music.stop()
        pygame.mixer.quit()
    finally:
        if os.path.exists(path):
            os.remove(path)

# دالة للتسجيل وحفظ الصوت من المايكروفون
def record_audio(filename="temp.wav"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ تفضل بالكلام...")
        audio = recognizer.listen(source)
        with open(filename, "wb") as f:
            f.write(audio.get_wav_data())
    return filename

# تحويل الصوت إلى نص باستخدام Whisper المحلي
def transcribe_with_whisper(filename="temp.wav"):
    try:
        result = whisper_model.transcribe(filename, language="ar")
        return result["text"]
    except Exception as e:
        print("❌ خطأ أثناء التحويل:", e)
        return ""

# الحصول على رد من Cohere
def get_reply(prompt):
    response = co.chat(message=prompt)
    return response.text

# البرنامج الرئيسي
def main():
    speak("أهلًا بك انا المساعد الصوتي الذكي! قل خروج لإنهاء المحادثة.")
    while True:
        audio_path = record_audio()
        user_text = transcribe_with_whisper(audio_path)
        if not user_text.strip():
            speak("لم أسمع جيدًا، حاول مرة أخرى.")
            continue
        print("👤 قلت:", user_text)
        if "خروج" in user_text or "انهاء" in user_text:
            speak("تم الإنهاء. إلى اللقاء!")
            break
        reply = get_reply(user_text)
        print("🤖   المساعد الصوتي الذكي:", reply)
        speak(reply)

if __name__ == "__main__":
    main()
