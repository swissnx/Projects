
#pip install pyfiglet
import pyfiglet
import webbrowser
import tempfile


class ASCIIArt:
    def __init__(self):
        self.__text = None
        self.__font = None

    def __create_ascii_art(self, text, font):
        ascii_art = pyfiglet.figlet_format(text=text, font=font)
        return ascii_art

    def __get_available_fonts(self):
        return [i for i in pyfiglet.FigletFont.getFonts()]

    def __show_available_fonts(self):
        return '\n'.join(self.__get_available_fonts())

    def run(self):
        try:
            show_fonts = input("List the available Fonts? (y/n): ")
            if show_fonts == "y":
                print(self.__show_available_fonts())

            while True:
                self.__text = input("\nEnter text: ")
                self.__font = input("Font: ")

                ascii_art = self.__create_ascii_art(self.__text, self.__font)
                print(ascii_art)

                continue_ = input("\nTry again? (y/n): ")
                if continue_.lower() != 'y':
                    break

        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"


if __name__ == "__main__":
    ascii_art = ASCIIArt()
    ascii_art.run()
