
import webbrowser as web


class DefineProfile(web.BackgroundBrowser):
    def __init__(self, path):
        super().__init__(path)

    def open(self, url, new=0, autoraise=True):
        args = [self.name + ' %s --profile-directory="Default"' % url]      # Find the User in the `Profile Path` field, here: `chrome://version/`
        #args = [self.name + ' %s --profile-directory="Profile 1"' % url]   # Replace `Profile 1` with the name of the specific user profile.
        #args = [self.name + ' %s --guest' % url]                           # Or name it `any_name` to create a new profile on the spot
        
        ''' Profile directory names are case-sensitive and must match the names of the directories in the Chrome
        user data directory (usually located at %LOCALAPPDATA%\Google\Chrome\User Data on Windows). '''
        if new == 0:
            web.Popen(args)
        elif new == 1:
            web.Popen(args + ['--new-window'])
        elif new == 2:
            web.Popen(args + ['--new-tab'])
        if autoraise:
            web.Popen(args + ['--raise-window'])


class InChromeOpener:
    def __init__(self):
        self.__chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
        self.__url_1 = 'https://www.example.com'
        self.__url_2 = 'https://www.google.com'

        web.register('chrome', None, DefineProfile(self.__chrome_path))

    def __open_urls(self):
        try:
            web.get('chrome').open(self.__url_1)
            web.get('chrome').open(self.__url_2)

            return "URLs opened successfully"
        except Exception as e:
            return f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m"

    def run(self):
        result = self.__open_urls()
        print(result)


if __name__ == "__main__":
    chrome_links = InChromeOpener()
    chrome_links.run()
