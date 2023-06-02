
import pyshorteners
from urllib.request import urlopen
from urllib.request import Request


class LinkShortener:
    def __init__(self):
        self.__shortener = pyshorteners.Shortener(api_key='e489e0bc9a09b1706f4413943293699471b63a5a')  # api_key='YOUR_API_KEY'

    def __link_shortener(self, link, service):
        if service == '1':
            short_link = self.__shortener.bitly.short(link)
        else:
            short_link = self.__shortener.tinyurl.short(link)
        return link, short_link

    def __link_opener(self, link):
        req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        shortenedUrl = urlopen(req)
        reallink = shortenedUrl.geturl()
        return link, reallink

    def __run(self):
        print("Enter your choice ...\n"
              "1. Shorten Link\n"
              "2. Get Real Link\n")
        action = input("\nChoice: ")

        if action == '1':
            print("Choose a service ...\n"
                  "1. bitly\n"
                  "2. tinyurl\n")
            service = input("\nService: ")
            link = input("Enter the link: ")
            real_link, short_link = self.__link_shortener(link, service)
            print('\n>> real link: ' + real_link)
            print('\n>> shortened link: ' + short_link)
        else:
            link = input("Enter the link: ")
            short_link, real_link = self.__link_opener(link)
            print('\n>> shortened link: ' + short_link)
            print('\n>> real link: ' + real_link)

    def run(self):
        self.__run()


if __name__ == "__main__":
    ls = LinkShortener()
    ls.run()
