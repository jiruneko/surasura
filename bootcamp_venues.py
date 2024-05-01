import requests

url = "https://www.pycon.jp/support/bootcamp.html"
result = requests.get(url)
result.encoding = result.apparent_encoding
print(result.text)