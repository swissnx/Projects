
import webbrowser as web


class DefineProfile(web.BackgroundBrowser):
    def __init__(self, path):
        super().__init__(path)

    def open(self, url, new=0, autoraise=True):
        args = [self.name + ' %s --profile-directory="Default"' % url]      # Find the User in the `Profile Path` field, here: `edge://version/`
        #args = [self.name + ' %s --profile-directory="Profile 1"' % url]   # Replace `Profile 1` with the name of the specific user profile.
        #args = [self.name + ' %s --guest' % url]                           # Or name it `any_name` to create a new profile on the spot
        
        ''' Profile directory names are case-sensitive and must match the names of the directories in the Edge
        user data directory (usually located at %LOCALAPPDATA%\Microsoft\Edge\User Data on Windows). '''
        if new == 0:
            web.Popen(args)
        elif new == 1:
            web.Popen(args + ['--new-window'])
        elif new == 2:
            web.Popen(args + ['--new-tab'])
        if autoraise:
            web.Popen(args + ['--raise-window'])


class InEdgeOpener:
    def __init__(self):
        self.__edge_path = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'
        self.__url_1 = 'https://www.example.com'
        self.__url_2 = 'https://www.google.com'

        web.register('edge', None, DefineProfile(self.__edge_path))

    def __open_urls(self):
        try:
            web.get('edge').open(self.__url_1)
            web.get('edge').open(self.__url_2)

            return "URLs opened successfully"
        
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def run(self):
        result = self.__open_urls()
        print(result)


if __name__ == "__main__":
    edge_links = InEdgeOpener()
    edge_links.run()
