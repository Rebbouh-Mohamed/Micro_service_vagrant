# app.py for microservice2
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# SQLAlchemy model for orders
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(80), nullable=False)

@app.route('/first')
def init_db():
    db.create_all()
    if not Order.query.first():
        db.session.add_all([Order(item="Order1"), Order(item="Order2"), Order(item="Order3")])
        db.session.commit()

@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify({"orders": [{"id": order.id, "item": order.item} for order in orders]})

@app.route('/')
def order_page():
    orders = Order.query.all()
    return render_template('orders.html', orders=orders)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
