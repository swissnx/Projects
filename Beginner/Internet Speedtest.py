#pip install speedtest-cli

import speedtest

internetSpeed = speedtest.Speedtest()

print("\nMeasuring Internet Speed\n")
print(f"Download - {internetSpeed.download() / 1_000_000:.2f} Mbps")
print(f"Upload - {internetSpeed.upload() / 1_000_000:.2f} Mbps")


# fetching best server specified:
internetSpeed.get_servers([])
best_server = internetSpeed.get_best_server()
print(f"\n\nUsing server: {best_server['host']}")
print(f"Server location: {best_server['country']}")
print(f"Download - {internetSpeed.download() / 1_000_000:.2f} Mbps")
print(f"Upload - {internetSpeed.upload() / 1_000_000:.2f} Mbps")
