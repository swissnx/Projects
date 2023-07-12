
import requests
import hashlib


class PasswordChecker:
    def __init__(self):
        self.__api_url = "https://api.pwnedpasswords.com/range/"

    def __request_api_data(self, query_char):
        try:
            url = self.__api_url + query_char
            res = requests.get(url)
            if res.status_code != 200:
                raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
            return res
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def request_api_data(self, query_char):
        return self.__request_api_data(query_char)

    @staticmethod
    def __get_password_leaks_count(hashes, hash_to_check):
        try:
            hashes = (line.split(':') for line in hashes.text.splitlines())
            for h, count in hashes:
                if h == hash_to_check:
                    return count
            return 0
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    @staticmethod
    def get_password_leaks_count(hashes, hash_to_check):
        return PasswordChecker.__get_password_leaks_count(hashes, hash_to_check)

    def __pwned_api_check(self, password):
        try:
            sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
            first5_char, tail = sha1password[:5], sha1password[5:]
            response = self.__request_api_data(first5_char)
            return self.__get_password_leaks_count(response, tail)
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def pwned_api_check(self, password):
        return self.__pwned_api_check(password)

    def __run(self):
        try:
            password = input("Check: ")
            count = self.__pwned_api_check(password)
            if count:
                print(f'{password} was found {count} times... You should probably change your password')
            else:
                print(f'{password} was NOT found. Carry on!')
            return 'done!'
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def run(self):
        return self.__run()


if __name__ == '__main__':
    password_checker = PasswordChecker()
    password_checker.run()
