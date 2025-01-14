__author__ = "Idan Talker"
__version__ = "1.0.1"
__maintainer__ = "Idan Talker"
__email__ = ["talkeridan@gmail.com"]
__status__ = "Prototype"

import speech_recognition as sr

class ASRModule:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def transcribe_from_speakers(self):
        with sr.Microphone() as source:
            print("Listening to speakers...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

    def start_continuous_transcription(self, callback):
        with sr.Microphone() as source:
            print("Continuous listening started...")
            self.recognizer.adjust_for_ambient_noise(source)
            
            while True:
                try:
                    audio = self.recognizer.listen(source)
                    text = self.recognizer.recognize_google(audio)
                    callback(text)
                except sr.UnknownValueError:
                    pass
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")
                except Exception as e:
                    print(f"An error occurred: {e}")



