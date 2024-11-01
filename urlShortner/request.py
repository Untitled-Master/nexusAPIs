import requests

url = 'http://127.0.0.1:5000/'  # URL of the Flask app
data = {
    "url": "https://news.djcity.com/wp-content/uploads/2017/08/rafik-600.jpg"  # The URL you want to shorten
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Shortened URL:", response.json())
else:
    print("Error:", response.status_code, response.text)
