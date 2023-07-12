
import wget


class FileDownloader:
    def __init__(self):
        self.__url = input("File URL: ")

    def __run(self):
        try:
            filename = wget.download(self.__url)
            print(f"\nDownloaded file: {filename}")
        
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def run(self):
        return self.__run()


if __name__ == "__main__":
    downloader = FileDownloader()
    filename = downloader.run()
