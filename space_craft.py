from typing import List
from marshmallow import Schema,fields

class Spaceship:
    def __init__(self, spaceship_id, name, type_, status="available"):
        self.spaceship_id = spaceship_id
        self.name = name
        self.type_ = type_
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

    def ship_info(self):
        return f"id : {self.spaceship_id}, name : {self.name}, type : {self.type_}, status : {self.status}"

_Spaceships = []
_Spaceships_dict = {}

class Mission:
    def __init__(self, mission_id, name, goal, status="planned"):
        self.mission_id = mission_id
        self.name = name
        self.goal = goal
        self.status = status
        self.spaceships = []

    def add_spaceship(self, spaceship):
        self.spaceships.append(spaceship)

    def update_status(self, new_status):
        self.status = new_status

    def mission_info(self):
        return f"id : {self.mission_id}, name : {self.name}, goal : {self.goal}, status : {self.status}"

_Missions = []
_MissionsDict = {}

class CrewMember:
    def __init__(self, member_id, name, role, spaceship):
        self.member_id = member_id
        self.name = name
        self.role = role                
        self.spaceship = spaceship

    def update_role(self, new_role):
        self.role = new_role

    def update_spaceship(self, new_spaceship):
        self.spaceship = new_spaceship

    def member_info(self):
        return f"id : {self.member_id}, name : {self.name}, role : {self.role}, spaceship : {self.spaceship}"


_CrewMembers: List[CrewMember] = []

class SpaceshipSchema(Schema):
    spaceship_id = fields.Integer(required=True)
    name = fields.Str(required=True)
    type = fields.Str(required=True)
    status = fields.Str() 


class MissionsSchema(Schema):    
    mission_id = fields.Integer(required=True)
    name = fields.Str(required=True)
    goal = fields.Str(required=True)
    status = fields.Str()
    
