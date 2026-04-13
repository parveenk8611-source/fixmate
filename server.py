from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = []

@app.route('/')
def home():
    return "FixMate Server Running"

@app.route('/add-user', methods=['POST'])
def add_user():
    user = request.json
    users.append(user)
    return jsonify({"status": "success"})

@app.route('/get-users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/admin-login', methods=['POST'])
def admin_login():
    data = request.json
    if data['username'] == 'admin' and data['password'] == 'fixmate123':
        return jsonify({"status": "success"})
    return jsonify({"status": "failed"})

app.run(host="0.0.0.0", port=5000)
