
def create_acronym(text: str) -> str:
    words = text.split()
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    return acronym


try:
    text = input("Enter here: ")
    acronym = create_acronym(text)
    print(f"\n'{text}' acronym: {acronym}")

except Exception as e:
    print(f"Problem is: {e}")
