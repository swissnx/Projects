
import pyshorteners
from urllib.request import urlopen
from urllib.request import Request


class LinkShortener:
    def __init__(self):
        self.__shortener = pyshorteners.Shortener(api_key='e489e0bc9a09b1706f4413943293699471b63a5a')  # api_key='YOUR_API_KEY'

    def __link_shortener(self, link, service):
        if service == '1':
            short_link = self.__shortener.bitly.short(link)
        elif service == '2':
            short_link = self.__shortener.tinyurl.short(link)
        return link, short_link

    def __link_opener(self, link):
        req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        shortenedUrl = urlopen(req)
        reallink = shortenedUrl.geturl()
        return link, reallink

    def run(self):
        while True:
            print("\n1. Shorten Link\n2. Get Real Link\n0. Exit")
            
            try:
                action = input("\nChoice: ")

                if action == '1':
                    print("\n1. bitly\n2. tinyurl")
                    service = input("\nService: ")
                    link = input("Link: ")
                    real_link, short_link = self.__link_shortener(link, service)

                    print('\n>> real link: ' + real_link)
                    print('\n>> shortened link: ' + short_link)

                elif action == "2":
                    link = input("\nLink: ")
                    short_link, real_link = self.__link_opener(link)

                    print('\n>> shortened link: ' + short_link)
                    print('\n>> real link: ' + real_link)

                elif action == '0' or action == "":
                    break
            
            except Exception as e:
                return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"


if __name__ == "__main__":
    ls = LinkShortener()
    ls.run()
