
import subprocess


class WifiPasswordRetriever:
    def __init__(self):
        self.__wifi_passwords = {}

    def __get_wifi_passwords(self):
        try:
            data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
            profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

            for profile in profiles:
                try:
                    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')
                    password = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                    if password:
                        self.__wifi_passwords[profile] = password[0]
                    else:
                        self.__wifi_passwords[profile] = None
                except subprocess.CalledProcessError:
                    print(f"An error occurred while retrieving the password for profile {profile}")
                    self.__wifi_passwords[profile] = None
        except subprocess.CalledProcessError:
            print("An error occurred while retrieving the WiFi profiles")
            return {}
    
    def get_wifi_passwords(self):
        return self.__get_wifi_passwords()

    def __run(self):
        try:
            self.__get_wifi_passwords()
            for profile, password in self.__wifi_passwords.items():
                if password:
                    print(f"{profile:<30} | {password}")
                else:
                    print(f"{profile:<30} | Password not found")
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def run(self):
        return self.__run()


if __name__ == '__main__':
    wifi_pass_retriever = WifiPasswordRetriever()
    wifi_pass_retriever.run()


# retrieves and displays the Wi-Fi passwords that are already stored on pc