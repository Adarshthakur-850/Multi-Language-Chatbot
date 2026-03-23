from .nlp.utils import NLPUtils
from .nlp.intent import IntentClassifier
from .nlp.retrieval import KnowledgeRetriever
from langdetect import detect

class ChatbotEngine:
    def __init__(self, faq_path):
        self.nlp = NLPUtils()
        self.intent_clf = IntentClassifier()
        self.retriever = KnowledgeRetriever(faq_path)

        training_data = []
        for item in self.retriever.data:
            training_data.append((item['question'], item['intent']))

        training_data.extend([
            ("hi", "greeting"),
            ("hello", "greeting"),
            ("hey", "greeting"),
            ("good morning", "greeting"),
            ("bye", "goodbye"),
            ("goodbye", "goodbye"),
            ("see you", "goodbye")
        ])

        self.intent_clf.train(training_data)

    def process_message(self, user_text):
        try:
            lang_code = detect(user_text)
        except:
            lang_code = 'en'

        if lang_code != 'en':
            english_text = self.nlp.detect_and_translate(user_text)
        else:
            english_text = user_text

        answer = self.retriever.get_best_match(english_text)

        if not answer:
            intent = self.intent_clf.predict(english_text)
            if intent == 'greeting':
                answer = "Hello! I am your support assistant. How can I help you?"
            elif intent == 'goodbye':
                answer = "Goodbye! Have a great day."
            else:
                answer = "I'm sorry, I didn't understand that. Could you rephrase?"

        final_response = self.nlp.translate_response(answer, lang_code)

        return {
            "original_text": user_text,
            "detected_lang": lang_code,
            "translated_text": english_text,
            "response": final_response
        }
