from flask import Blueprint, request, jsonify
from sqli import create, read_all, read_one, update, complete, delete


# MAIN ROUTER
main = Blueprint('main', __name__)


# Route to get all data


@main.route('/', methods=['GET'])
def get_all_data():
    data = read_all()
    return jsonify(data)

# Route to add new data


@main.route('/', methods=['POST'])
def add_data():
    print(request)
    req_data = request.json
    print(req_data)
    print(req_data["name"])
    create(req_data["name"])
    return jsonify({"task": "added"}), 201

# Route to update data


@main.route('/<int:id>', methods=['PUT'])
def update_data(id):
    if read_one(id) == None:
        return jsonify({"error": "Not found"}), 404
    new_data = request.json
    update(id, new_data['name'], 0)
    return jsonify({"task": "updated"}), 202


@main.route('/<int:id>', methods=['PATCH'])
def comlete_task(id):
    if read_one(id) == None:
        return jsonify({"error": "Not found"}), 404
    complete(id)
    return jsonify({"task": "completed"}), 202


# Route to delete data
@main.route('/<int:id>', methods=['DELETE'])
def delete_data(id):
    if read_one(id) == None:
        return jsonify({"error": "Not found"}), 404
    delete(id)
    return jsonify({"task": "deleted"}), 202
