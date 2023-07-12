
import emoji
import demoji

class EmojiConverter:
    def __init__(self):
        self.__options = {"1": self.__text_to_emoji,
                          "2": self.__emoji_to_text,
                          "3": self.__list_all_emojis,
                          "4": self.__emoji_list,
                          "5": self.__distinct_emoji_list,
                          "6": self.__emoji_count,
                          "7": self.__is_emoji,
                          "8": self.__version,
                          "9": self.__search_emoji
                          }
        self.__custom_codes = {":D": "\U0001F600",
                                    ":p": "\U0001F61B",
                                    # add more custom shortcodes here from below:
                                    # https://unicode.org/emoji/charts/full-emoji-list.html
                                    # it is always \U0000 +all_unicode_code_nums
                                    # https://unicode.org/Public/emoji/15.0/
                                    }

    def __text_to_emoji(self, text: str) -> str:
        return emoji.emojize(text)

    def __emoji_to_text(self, text: str) -> str:
        return demoji.replace_with_desc(text)

    def __list_all_emojis(self) -> str:
        all_emojis = ""
        for key in emoji.EMOJI_DATA.keys():
            all_emojis += f"{key}: {emoji.emojize(key)}: {emoji.demojize(emoji.emojize(key))}\n"
        return all_emojis

    def __emoji_list(self, text: str) -> str:
        return emoji.emoji_list(text)

    def __distinct_emoji_list(self, text: str) -> str:
        return emoji.distinct_emoji_list(text)

    def __emoji_count(self, text: str) -> int:
        return emoji.emoji_count(text)

    def __is_emoji(self, text: str) -> bool:
        return emoji.is_emoji(text)

    def __version(self, text: str) -> str:
        return emoji.version(text)

    def __search_emoji(self, keyword: str) -> str:
        if keyword in self.__custom_codes:
            return self.__custom_codes[keyword]
        else:
            return "Emoji not found"

    def run(self):
        while True:
            print("1. Text to Emoji\n2. Emoji to Text\n3. List all Emojis")
            print("4. Locate all Emojis in a string")
            print("5. Distinct list of emojis in a string")
            print("6. Number of emojis in a string")
            print("7. Check if single emoji")
            print("8. Find Unicode version of an emoji")
            print("9. Search with a short keyword")
            print("0. Exit")

            try:
                choice = input("\nChoice: ")

                if choice == '0' or choice == "":
                    break
                
                if choice in ['1', '2']:
                    text = input("\nEnter text: ")
                    result = self.__options[choice](text)
                    print(f"\nResult: {result}")

                elif choice == '3':
                    result = self.__options[choice]()
                    print(f"\n{result}")

                elif choice in ['4', '5', '6', '7', '8']:
                    text = input("\nEnter text: ")
                    result = self.__options[choice](text)
                    print(f"\nResult: {result}")

                elif choice == '9':
                    keyword = input("\nEnter keyword: ")
                    result = self.__options[choice](keyword)
                    print(f"\nResult: {result}")
                    
                else:
                    print("\nInvalid choice")

            except ValueError as ve:
                return f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m"

            except Exception as e:
                return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"


if __name__ == "__main__":
    emoji_converter = EmojiConverter()
    emoji_converter.run()



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# https://carpedm20.github.io/emoji/docs/