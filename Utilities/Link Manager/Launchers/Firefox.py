
import webbrowser as web


class DefineProfile(web.BackgroundBrowser):
    def __init__(self, path):
        super().__init__(path)

    def open(self, url, new=0, autoraise=True):
        args = [self.name + ' %s -P "default"' % url]      # Find the User in the `Profile Path` field, here: `about:profiles`
        #args = [self.name + ' %s -P "Profile 1"' % url]   # Replace `Profile 1` with the name of the specific user profile.
        #args = [self.name + ' -private-window %s' % url]  # Open URL in private browsing mode
        
        ''' Profile names are case-sensitive and must match the names of the profiles in the Firefox
        user data directory (usually located at %APPDATA%\Mozilla\Firefox\Profiles on Windows). '''
        if new == 0:
            web.Popen(args)
        elif new == 1:
            web.Popen(args + ['--new-window'])
        elif new == 2:
            web.Popen(args + ['--new-tab'])
        if autoraise:
            web.Popen(args + ['--raise-window'])


class InFirefoxOpener:
    def __init__(self):
        self.__firefox_path = 'C:/Program Files/Mozilla Firefox/firefox.exe'
        self.__url_1 = 'https://www.example.com'
        self.__url_2 = 'https://www.google.com'

        web.register('firefox', None, DefineProfile(self.__firefox_path))

    def __open_urls(self):
        try:
            web.get('firefox').open(self.__url_1)
            web.get('firefox').open(self.__url_2)

            return "URLs opened successfully"
        
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def run(self):
        result = self.__open_urls()
        print(result)


if __name__ == "__main__":
    firefox_links = InFirefoxOpener()
    firefox_links.run()
