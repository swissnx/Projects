
#pip install langdetect
from langdetect import detect, LangDetectException


class LanguageDetector:
    def __init__(self):
        pass

    def __detect_language(self, text: str) -> str:
        try:
            language = detect(text)
            return language
        except LangDetectException:
            return "Error: Unable to detect language"

    def detect_language(self, text: str) -> str:
        return self.__detect_language(text)

    def run(self):
        print("\n1. Enter text in any language to detect the language.\n0. Exit")
        
        while True:
            try:

                text = input("\nText: ")

                if text == '0' or text == "":
                    break
                
                language = self.__detect_language(text)
                print(f"\nThe detected: {language}")
            
            except Exception as e:
                return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"


if __name__ == "__main__":
    language_detector = LanguageDetector()
    language_detector.run()
