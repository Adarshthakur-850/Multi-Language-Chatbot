import re
from deep_translator import GoogleTranslator

class NLPUtils:
    def __init__(self):
        self.translator = GoogleTranslator(source='auto', target='en')

    def detect_and_translate(self, text):
        """
        Translates text to English and returns the original language code.
        """
        try:

            translated = self.translator.translate(text)
            return translated
        except Exception as e:
            print(f"Translation Error: {e}")
            return text

    def translate_response(self, text, target_lang):
        """
        Translates text from English to target language.
        """
        if target_lang == 'en':
            return text
        try:
            return GoogleTranslator(source='en', target=target_lang).translate(text)
        except Exception as e:
            print(f"Response Translation Error: {e}")
            return text

    def preprocess(self, text):
        """
        Basic cleaning: lowercase, remove special chars.
        """
        text = text.lower()
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        return text
