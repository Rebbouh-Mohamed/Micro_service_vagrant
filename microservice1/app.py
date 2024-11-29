# app.py for microservice1
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# SQLAlchemy model for users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

@app.route('/first', methods=['GET'])
def init_db():
    db.create_all()
    if not User.query.first():
        db.session.add_all([User(name="Alice"), User(name="Bob"), User(name="Charlie")])
        db.session.commit()

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify({"users": [{"id": user.id, "name": user.name} for user in users]})

@app.route('/')
def user_page():
    users = User.query.all()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
