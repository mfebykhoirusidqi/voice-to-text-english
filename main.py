import speech_recognition as sr
from googletrans import Translator


# Membuat instance recognizer, translator, dan stemmer 
# Create recognizer, translator, and stemmer instances
r = sr.Recognizer()
translator = Translator()
# Membaca suara dari microphone
# Read voice from microphone
with sr.Microphone() as source:
    print("Let's Talk...")
    audio = r.listen(source)

try:
    # Mengubah suara menjadi teks dalam bahasa Inggris
    text = r.recognize_google(audio, language='en-US')
    print(f"Text in English: {text}")

except sr.UnknownValueError:
    print("Google Speech Recognition tidak mengerti audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")

