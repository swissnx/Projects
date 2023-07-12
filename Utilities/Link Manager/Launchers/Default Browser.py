
import webbrowser as web


class DefaultBrowser:
    def __init__(self):
        self.__url_1 = 'https://www.example.com'
        self.__url_2 = 'https://www.google.com'

    def __open_urls(self):
        try:
            web.open(self.__url_1)
            web.open(self.__url_2)
            
            return "URLs opened successfully"
        
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def run(self):
        result = self.__open_urls()
        print(result)


if __name__ == "__main__":
    default_browser = DefaultBrowser()
    default_browser.run()
