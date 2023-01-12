import speech_recognition as sr
from google_trans_new import google_translator
from gtts import gTTS
from playsound import playsound
import os

r = sr.Recognizer()
translator = google_translator()

print(sr.Microphone.list_microphone_names())

# translate_text = translator.translate('สวัสดีจีน',lang_tgt='en')
# print(translate_text)

while True:
    with sr.Microphone(device_index=1) as source:
        print("speak now:")
        audio = r.listen(source)
        try:
            speech_text = r.recognize_google(audio, language='fr')
            print(speech_text)
            if (speech_text == "exit"):
                break
        except sr.UnknownValueError:
            print("Could not understand")
        except sr.RequestError:
            print('Could not request result from google')

        translated_text = translator.translate(text=speech_text, lang_src='fr', lang_tgt='en')
        print(translated_text)

        voice = gTTS(translated_text, lang='en')
        voice.save("voice.mp3")
        playsound("voice.mp3")
        os.remove("voice.mp3")
