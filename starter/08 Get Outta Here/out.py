# Create a simple API that have one endpoint (remove user) that receives id from a user list
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample user list
users = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Jane"},
    {"id": 3, "name": "Alice"}
]

@app.route('/remove_user', methods=['POST'])
def remove_user():
    user_id = request.json.get('id')

    if user_id is None:
        return jsonify({'error': 'User ID is required'}), 400

    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            return jsonify({'message': 'User removed successfully'})

    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run()