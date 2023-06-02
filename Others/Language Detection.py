
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

    def __prompt(self):
        while True:
            text = input("\nText: ")
            if text.lower() == 'q' or text.lower() == "":
                break
            language = self.__detect_language(text)
            print(f"\nThe detected language is: {language}")

    def prompt(self):
        return self.__prompt()

    def run(self):
        print("Enter any text in any language for the program to detect the language.\nOr press \"Q\" to exit the program")
        self.__prompt()


if __name__ == "__main__":
    language_detector = LanguageDetector()
    language_detector.run()
