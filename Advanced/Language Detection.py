
#pip install langdetect

from langdetect import detect, LangDetectException

def detect_language(text: str) -> str:
    try:
        language = detect(text)
        return language
    except LangDetectException:
        return "Error: Unable to detect language"

def prompt():
    while True:
        text = input("\nText: ")
        if text.lower() == 'q':
            break
        language = detect_language(text)
        print(f"\nThe detected language is: {language}")

if __name__ == '__main__':
    print("Enter any text in any language for the program to detect the language.\nOr press \"Q\" to exit the program")
    prompt()
