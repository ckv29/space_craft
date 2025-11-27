from space_craft import Spaceship, _Spaceships, Mission, _Missions, CrewMember, _CrewMembers, _Spaceships_dict,_MissionsDict
def get_ships_list():
    return ", ".join(_Spaceships)

def add_ship(spaceship_id, name, type_, status="available"):
    new_ship = Spaceship(spaceship_id, name, type_, status)
    _Spaceships.append(name)
    _Spaceships_dict[name]=new_ship
    return "ok"

# обновляем по name, а не по id для наглядности
def update_ship_status(name, new_status):
    ship = _Spaceships_dict.get(name)
    if ship is not None:
        ship.status = new_status
        return "ok"
    else:
        return "not found"
   

def delete_ship(name):
    ship = _Spaceships_dict.get(name)
    if ship is not None:
        _Spaceships.remove(name)
        del _Spaceships_dict[name]
        return "ok"
    else:
        return "not found"

def get_missions_list():    
    return ", ".join(_MissionsDict)


def add_mission(id,name,goal,status):
    new_mission = Mission(id,name,goal,status)
    _Missions.append(new_mission)
    _MissionsDict[name]=new_mission
    return "ok"


def add_ship_to_mission(mission_name, ship_name):
    mission = _MissionsDict.get(mission_name)
    if mission is not None:
        mission.spaceships.append(ship_name)
        return "ok"
    else:
        return "not found"


def update_mission_status(name, new_status):
    mission = _MissionsDict.get(name)
    if mission is not None:
        mission.status = new_status
        return "ok"
    else:
        return "not found"
   

def delete_mission(name):
    mission = _MissionsDict.get(name)
    if mission is not None:
        _Missions.remove(name)
        del _MissionsDict[name]
        return "ok"
    else:
        return "not found"


add_ship(1,"Millenium Falcon","YT-1300")

add_ship(2,"blue seagull","111")
