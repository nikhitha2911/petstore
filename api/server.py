from flask import Flask, jsonify, request
import json
from collections import OrderedDict
APP = Flask(__name__)
pets={}
@APP.route('/')
def hello_world():
    return 'welcome'

@APP.route("/pet", methods=["POST"])
def post():
    pet_data=request.data
    parsed_pet_data=json.loads(pet_data)
    id=parsed_pet_data["id"]
    if id not in pets:
        pets[id]=pet_data
        return jsonify(request.get_json()), 200
    else:
        return jsonify({"status": "Data already exists",}), 200

@APP.route("/pet/<int:pet_id>", methods=["GET"])
def get(pet_id):
    if pet_id in pets:
        return jsonify(json.loads(pets[pet_id])), 200
    else:
        return jsonify({
  "code": 1,
  "type": "error",
  "message": "Pet not found"
}), 404

@APP.route("/pet", methods=["PUT"])
def put():
    pet_data = request.data
    parsed_pet_data = json.loads(pet_data)
    id = parsed_pet_data["id"]
    if id in pets:
        pets[id] = pet_data
        return jsonify(request.get_json()), 200
    else:
        return jsonify({
  "code": 1,
  "type": "error",
  "message": "Pet not found"
}), 404

@APP.route("/pet/<int:pet_id>", methods=["DELETE"])
def delete(pet_id):
    if pet_id in pets:
        del pets[pet_id]
        return jsonify({"status": "Successfully deleted pet object",}), 200
    else:
        return jsonify({
  "code": 1,
  "type": "error",
  "message": "Pet not found"
}), 404


@APP.route("/pet/<int:pet_id>", methods=["POST"])
def update_existing_record(pet_id):
    pet_data = request.data
    status = request.args.get("status")
    name = request.args.get("name")

    if pet_id in pets:

        pet_data=pets[pet_id]
        parsed_pet_data=json.loads(pet_data)
        parsed_pet_data['name']=name
        parsed_pet_data['status']=status
        pets[pet_id]=json.dumps(parsed_pet_data)
        return jsonify(request.get_json()), 200
    else:
        return jsonify({
  "code": 1,
  "type": "error",
  "message": "Pet not found"
}), 404

@APP.route("/pet/findByStatus", methods=["GET"])
def find_by_status():
    pets_by_status = []
    status=request.args.get("status")
    for key,value in  pets.items():
        pet_data=json.loads(value)
        if str(pet_data["status"])==str(status):
            pets_by_status.append(pet_data)
    return jsonify(pets_by_status)

if __name__ == "__main__":
    APP.run(debug=True)
    APP.config['JSON_SORT_KEYS'] = False


