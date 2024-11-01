from flask import Flask, request, redirect, jsonify
import string
import random


url_mapping = {}

def code():
    res = ''.join(random.choices(string.ascii_letters,k=7))
    u = str(res)
    return u

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
    u = code()
    data = request.json.get('url')
    url_mapping[u] = data
    return jsonify({"short_url": request.host_url + u})


@app.route('/<short_url>')
def redirect_to_original(short_url):
    original_url = url_mapping.get(short_url)
    if original_url:
        return redirect(original_url)
    else:
        return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)
