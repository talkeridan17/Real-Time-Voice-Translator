__author__ = "Idan Talker"
__version__ = "1.0.1"
__maintainer__ = "Idan Talker"
__email__ = ["talkeridan@gmail.com"]
__status__ = "Prototype"

from libretranslatepy import LibreTranslateAPI

class TranslationModule:
    def __init__(self):
        try:
            self.translator = LibreTranslateAPI("https://libretranslate.com/", api_key="your_api_key_here") # Add API key here
        except Exception as e:
            print(f"Error initializing translator: {str(e)}")
            self.translator = None

    def translate(self, text, source_lang, target_lang):
        if not self.translator:
            print("Translator not initialized")
            return None
        try:
            return self.translator.translate(text, source_lang, target_lang)
        except Exception as e:
            print(f"Translation error: {str(e)}")
            return None

    def get_supported_languages(self):
        if not self.translator:
            print("Translator not initialized")
            return []
        try:
            return self.translator.languages()
        except Exception as e:
            print(f"Error fetching supported languages: {str(e)}")
            return []


