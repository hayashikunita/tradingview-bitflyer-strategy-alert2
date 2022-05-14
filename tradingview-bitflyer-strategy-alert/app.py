import json, config
from flask import Flask, request, render_template
import ccxt
import settings

app = Flask(__name__)


import urllib.request
import json
import pprint



@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    #print(request.data)
    data = json.loads(request.data)

    if data['passphrase'] != config.WEBHOOK_PASSPHRASE:
        return {
            "code": "error",
            "message": "Nice try, invalid passphrase"
        }

    side = data['strategy']['order_action']
    bitflyer = ccxt.bitflyer()
    bitflyer.apiKey = settings.apiKey
    bitflyer.secret=  settings.secret

    order = bitflyer.create_order(
        symbol = 'BTC/JPY',
        type='market',
        side= side,
        amount='0.01',
        price='0',
        # params = { "product_code" : settings.product_code })
        params = { "product_code" : "BTC_JPY" })

    order_response =  order

    if order_response:
        return {
            "code": "success",
            "message": "order executed"
        }
    else:
        print("order failed")

        return {
            "code": "error",
            "message": "order failed"
        }


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')