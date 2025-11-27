from logic import get_ships_list,add_ship,update_ship_status,delete_ship,get_missions_list,add_mission,update_mission_status,add_ship_to_mission,delete_mission
from flask import Flask,request,jsonify
from space_craft import SpaceshipSchema,MissionsSchema
from marshmallow import ValidationError


app = Flask(__name__)

spaceship_schema = SpaceshipSchema()

missions_schema = MissionsSchema()

@app.route('/api/v1', methods=['GET'])
def home():
    return "Сервер работает!", 200


@app.get('/api/v1/shiplist')
def get_ships_list_controller():
    ships = get_ships_list()
    return ships, 200   


@app.post('/api/v1/addship')
def add_ship_controller():
    try:
        data = spaceship_schema.load(request.get_json())
    except ValidationError as err:
        return jsonify({"error": "Validation failed", "messages": err.messages}), 400
 
    spaceship_id = data['spaceship_id']
    name = data['name']
    type_ = data['type']
    status = data['status']

    result = add_ship(spaceship_id, name, type_, status)

    if result == "ok":
        return jsonify({"message": "Spaceship added successfully"}), 201
    else:
        return jsonify({"error": "Failed to add spaceship"}), 500


@app.get('/api/v1/shipstatus/<ship>/<newstatus>')
def update_ship_status_controller(ship,newstatus):   
    result = update_ship_status(ship,newstatus)
    if result == "ok":
        return jsonify({"message": "Status updated successfully"}), 201
    elif result == "not found":
        return jsonify({"message": "Ship not found"}), 404
    else:
        return jsonify({"error": "Failed to update status"}), 500


@app.delete('/api/v1/deleteship/<ship>')
def delete_ship_controller(ship):
    result = delete_ship(ship)
    if result == "ok":
        return jsonify({"message": "Ship deleted successfully"}), 201
    elif result == "not found":
        return jsonify({"message": "Ship not found"}), 404
    else:
        return jsonify({"error": "Failed to delete ship"}), 500


@app.get('/api/v1/missionslist')
def get_missions_list_controller():
    missions = get_missions_list()
    return missions, 200   


@app.post('/api/v1/addmission')
def add_mission_controller():
    try:
        data = missions_schema.load(request.get_json())
    except ValidationError as err:
        return jsonify({"error": "Validation failed", "messages": err.messages}), 400
 
    mission_id = data['mission_id']
    name = data['name']
    goal = data['goal']
    status = data['status']

    result = add_mission(mission_id,name,goal,status)

    if result == "ok":
        return jsonify({"message": "Mission added successfully"}), 201
    else:
        return jsonify({"error": "Failed to add missions"}), 500


@app.get('/api/v1/missionstatus/<mission>/<newstatus>')
def update_mission_status_controller(mission,newstatus):   
    result = update_mission_status(mission,newstatus)
    if result == "ok":
        return jsonify({"message": "Status updated successfully"}), 201
    elif result == "not found":
        return jsonify({"message": "Mission not found"}), 404
    else:
        return jsonify({"error": "Failed to update status"}), 500


@app.delete('/api/v1/deletemission/<mission>')
def delete_mission_controller(mission):
    result = delete_mission(mission)
    if result == "ok":
        return jsonify({"message": "Mission deleted successfully"}), 201
    elif result == "not found":
        return jsonify({"message": "Mission not found"}), 404
    else:
        return jsonify({"error": "Failed to delete mission"}), 500


@app.get('/api/v1/missionaddship/<mission>/<ship>')
def add_ship_to_mission_controller(mission,ship):   
    result = add_ship_to_mission(mission,ship)
    if result == "ok":
        return jsonify({"message": "Ship added successfully"}), 201
    elif result == "not found":
        return jsonify({"message": "Mission not found"}), 404
    else:
        return jsonify({"error": "Failed to update status"}), 500



if __name__ == "__main__":
    app.run(debug=True)

