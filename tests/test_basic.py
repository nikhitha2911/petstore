"""Basic Tests"""
import json






def test_post_pet_data(api_client):
    data={
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
    with api_client as client:
        assert 200  == client.post("/pet",json=data).status_code
        assert b'{"status":"Data already exists"}\n' == client.post("/pet", json=data).data


def test_get_pet_data(api_client):
    data = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    with api_client as client:
        #print(client.get("/pet/0").data)
        parsed_pet=json.loads(client.get("/pet/0").data)
        assert 0 == parsed_pet['id']

def test_put_pet_data(api_client):
    data={
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggies",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
    with api_client as client:
        assert 200  == client.put("/pet",json=data).status_code
        parsed_pet = json.loads(client.get("/pet/0").data)
        assert 'doggies' == parsed_pet['name']

def test_delete_pet_data(api_client):
    data = {
        "id": 1,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    with api_client as client:
        #print(client.get("/pet/0").data)
        client.post("/pet", json=data).data
        assert 1 == json.loads(client.get("/pet/1").data)['id']

        assert 200 ==client.delete("/pet/1").status_code

        assert {"code": 1,"type": "error","message": "Pet not found"}==client.get("/pet/1").get_json()