
class CreateAcronym:
    def __init__(self, text: str) -> str:
        self.__text = text
    
    def create_acronym(self):
        words = self.__text.split()
        acronym = ""
        for word in words:
            acronym += word[0].upper()
        return acronym

text = input("Enter here: ")

acronym = CreateAcronym(text)

try:
    result = acronym.create_acronym()
    print(f"\n'{text}' acronym: {result}")

except Exception as e:
    print(f"Problem is: {e}")
