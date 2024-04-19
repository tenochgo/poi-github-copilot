# /fix there is duplicated code here and it is not necessary to have it 
from flask import Flask, jsonify, request

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

# Endpoint to insert a user
@app.route('/insert_user', methods=['POST'])
def insert_user():
    data = request.get_json()
    name = data['name']
    age = data['age']
    # Generate a unique ID for the user
    user_id = len(users) + 1
    user = {'id': user_id, 'name': name, 'age': age}
    users.append(user)
    return jsonify({'id': user_id, 'user_count': len(users)})

# Endpoint to remove a user
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
    app.run(debug=True)
