
import wget

class FileDownloader:
    def __init__(self):
        self.__url = input("File URL: ")

    def __run(self):
        try:
            filename = wget.download(self.__url)
            return filename
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;196m{e}\u001b[0m")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    downloader = FileDownloader()
    filename = downloader.run()
    print(f"\nDownloaded file: {filename}")
