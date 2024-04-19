# Create a simple API that have two endpoints (get user, get users) that retrieves information about
# a collection of users and a specific user. and test it 

from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
users = [
    {"id": 1, "name": "John Doe", "age": 25},
    {"id": 2, "name": "Jane Smith", "age": 30},
    {"id": 3, "name": "Bob Johnson", "age": 35}
]

# Endpoint to get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Endpoint to get a specific user
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"message": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)