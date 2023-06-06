
import urllib.parse

url = input("URL to encode: ")
encoded_url = urllib.parse.quote(url, safe='')

print(f"\nEncoded URL: {encoded_url}")
