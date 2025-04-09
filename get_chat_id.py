import requests

BOT_TOKEN = "7901637126:AAGVBPWFYn1g6PbfLJ6IsbUotzAjeJqgxS0"
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"

response = requests.get(URL)
print(response.json())

