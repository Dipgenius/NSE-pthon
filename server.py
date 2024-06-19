import os
from flask import Flask
import requests
import json
app = Flask(__name__)
port = int(os.environ.get('PORT', 3000))
@app.route('/')
def hello():
   url = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'

   headers={'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
   response = requests.get(url, headers=headers, timeout=10)
   response_text=response.text
   print(response_text)
   json_object = json.loads(response_text)
   return json_object['filtered']['data']
@app.route('/top20')
def hello1():
   url = 'https://www.nseindia.com/api/liveEquity-derivatives?index=top20_contracts'

   headers={'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
   response = requests.get(url, headers=headers, timeout=10)
   response_text=response.text
   print(response_text)
   return response_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)