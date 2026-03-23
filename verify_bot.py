import sys
import os

sys.path.append(os.getcwd())

try:
    from src.chatbot import ChatbotEngine
    print("Import successful")
except ImportError as e:
    print(f"Import failed: {e}")
    sys.exit(1)

def test_bot():
    print("Initializing ChatbotEngine...")
    try:
        faq_path = os.path.join(os.getcwd(), 'data', 'faqs.json')
        bot = ChatbotEngine(faq_path)
        print("Bot initialized.")

        test_msg = "Hello"
        print(f"Testing message: {test_msg}")
        response = bot.process_message(test_msg)
        print("Response:", response)

        test_msg_es = "Hola" 
        print(f"Testing message: {test_msg_es}")
        response_es = bot.process_message(test_msg_es)
        print("Response ES:", response_es)

    except Exception as e:
        print(f"Runtime error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_bot()
