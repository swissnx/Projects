
import requests
import json


class AbuseIPDB:
    def __init__(self):
        self.__url = 'https://api.abuseipdb.com/api/v2/check'
        self.__headers = {'Accept': 'application/json',
                          'Key': '6ca068a91b7a3ceb1b2fd358d5f0539fb6f6c01036bfdfa94b96c0b1ac6b7b61716ab017ea5d0216'}

    def __get_response(self, ip):
        querystring = {'ipAddress': ip}
        response = requests.request(method='GET', url=self.__url, headers=self.__headers, params=querystring)
        return response

    def get_response(self, ip):
        return self.__get_response(ip)

    def __check_ip(self, ip):
        response = self.__get_response(ip)
        decodedResponse = json.loads(response.text)
        return json.dumps(decodedResponse, sort_keys=True, indent=4)

    def check_ip(self):
        return self.__check_ip()

    def __run(self):
        try:
            while True:
                print("1. Check IP\n0. Exit")
                choice = input('\nChoose: ')

                if choice == '1':
                    ip = input("URL/IP: ")
                    print(self.__check_ip(ip))
                    
                elif choice == '0' or choice == "":
                    break
                
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def run(self):
        return self.__run()


if __name__ == '__main__':
    ip_check = AbuseIPDB()
    ip_check.run()
