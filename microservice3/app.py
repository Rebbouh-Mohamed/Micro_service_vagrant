# app.py for microservice3
import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

USER_SERVICE_URL = 'http://10.0.2.15:5001/users'
ORDER_SERVICE_URL = 'http://10.0.2.15:5002/orders'

@app.route('/aggregated', methods=['GET'])
def aggregate():
    users = requests.get(USER_SERVICE_URL).json()
    orders = requests.get(ORDER_SERVICE_URL).json()
    return jsonify({"users": users["users"], "orders": orders["orders"]})

@app.route('/')
def aggregated_page():
    users = requests.get(USER_SERVICE_URL).json()["users"]
    orders = requests.get(ORDER_SERVICE_URL).json()["orders"]
    return render_template('aggregated.html', users=users, orders=orders)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
