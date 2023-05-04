
#pip install speedtest-cli

import speedtest

try:
    internetSpeed = speedtest.Speedtest()
    download = internetSpeed.download() / 1_000_000
    upload = internetSpeed.upload() / 1_000_000

    print("\nMeasuring Internet Speed\n")
    print(f"Download - {download:.2f} Mbps")
    print(f"Upload - {upload:.2f} Mbps")


    # fetching best server specified:
    internetSpeed.get_servers([])
    best_server = internetSpeed.get_best_server()
    host_server = best_server['host']
    country_server = best_server['country']
    
    print(f"\n\nUsing server: {host_server}")
    print(f"Server location: {country_server}")
    print(f"Download - {download:.2f} Mbps")
    print(f"Upload - {upload:.2f} Mbps")

except Exception as e:
    print(f"Problem is: {e}")

