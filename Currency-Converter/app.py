from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Route for home page
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        amount = float(request.form['amount'])
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']

        # Use Frankfurter API for currency conversion
        url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
        response = requests.get(url)
        data = response.json()

        result = data['rates'][to_currency]

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
