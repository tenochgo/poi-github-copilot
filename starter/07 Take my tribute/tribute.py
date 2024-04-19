# Create a simple API that have one endpoint (insert user) that receives information about a users and retrieves a generated id and the count of users inserted.
from flask import Flask, jsonify, request

app = Flask(__name__)

users = []
user_count = 0

@app.route('/insert_user', methods=['POST'])
def insert_user():
    global user_count
    data = request.get_json()
    name = data['name']
    age = data['age']
    # Generate a unique ID for the user
    user_id = len(users) + 1
    user = {'id': user_id, 'name': name, 'age': age}
    users.append(user)
    user_count += 1
    return jsonify({'id': user_id, 'user_count': user_count})

if __name__ == '__main__':
    app.run()