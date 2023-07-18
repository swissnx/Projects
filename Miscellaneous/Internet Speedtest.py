
#pip install speedtest-cli
from speedtest import Speedtest


class InternetSpeed:
    def __init__(self):
        self.__internet_speed = Speedtest()
        self.__download = self.__internet_speed.download() / 1_000_000
        self.__upload = self.__internet_speed.upload() / 1_000_000

    def __measure_speed(self):
        return (self.__download, self.__upload)
    
    def measure_speed(self):
        return self.__measure_speed()

    def __fetch_best_server(self):
        self.__internet_speed.get_servers([])
        best_server = self.__internet_speed.get_best_server()
        host_server = best_server['host']
        country_server = best_server['country']
        return (host_server, country_server)

    def fetch_best_server(self):
        return self.__fetch_best_server()

    def __run(self):
        try:
            download, upload = self.__measure_speed()
            print("\nMeasuring Internet Speed:\n")
            print(f"Download - {download:.2f} Mbps")
            print(f"Upload - {upload:.2f} Mbps")
            
            host_server, country_server = self.__fetch_best_server()
            print(f"\n\nUsing server: {host_server}")
            print(f"Server location: {country_server}")
            print(f"Download - {download:.2f} Mbps")
            print(f"Upload - {upload:.2f} Mbps")
            
        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    internet_speed = InternetSpeed()
    internet_speed.run()
