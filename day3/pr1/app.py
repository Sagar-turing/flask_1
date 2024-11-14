from flask import Flask, request, jsonify,render_template

app = Flask(__name__)

# Mock user for demonstration purposes
user = {
    "username": "user",
    "password": "pass"
}


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if username == user['username'] and password == user['password']:
        return jsonify(success=True), 200
    else:
        return jsonify(success=False), 401

if __name__ == '__main__':
    app.run(debug=True)