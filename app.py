from flask import request ,Flask,jsonify

app = Flask(__name__)

upi_currency = {
    'INR': {'USD': 0.012, 'CND': 0.016, 'AUD': 0.018, 'EUR': 0.011, 'GBP': 0.009},
    'USD': {'INR': 82.91, 'CND': 1.34, 'AUD': 1.49, 'EUR': 0.91, 'GBP': 0.78},
    'CAD': {'INR': 62.09, 'USD': 0.75, 'AUD': 1.12, 'EUR': 0.67, 'GBP': 0.58},
    'AUD': {'INR': 55.57, 'USD': 0.67, 'CND': 0.90, 'EUR': 0.60, 'GBP': 0.52},
    'EUR': {'INR': 88.71, 'USD': 1.09, 'CND': 1.49, 'AUD': 1.67, 'GBP': 0.86},
    'GBP': {'INR': 110.56, 'USD': 1.28, 'CND': 1.72, 'AUD': 1.92, 'EUR': 1.16}
}

@app.route('/',methods=['POST'])
def index():
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']
    print(data)
    print(source_currency)
    print(amount)
    print(target_currency)

    to_curDict = upi_currency[source_currency]
    if to_curDict:
        con_value = to_curDict[target_currency]
        con_amount = amount * con_value
    else:
        pass

    print(con_amount)


    response = {
        'fulfillmentText': "{}  {} is {} {}".format(amount,source_currency,con_amount,target_currency)
    }
    print(response['fulfillmentText'])
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)