from flask import Flask, jsonify, request

app = Flask(__name__)


users = {
    "jane": {"username": "jane", "name": "Jane",
             "age": 28, "city": "Los Angeles"},

    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}),

    username = data['username']
    if username in users:
        return jsonify({"error": "User already exists"}),

    users[username] = {
        "username": username,
        "name": data.get('name', ''),
        "age": data.get('age', 0),
        "city": data.get('city', '')
    }

    return jsonify({"message": "User added", "user": users[username]}),


if __name__ == "__main__":
    app.run(debug=True)
