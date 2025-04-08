from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def save(self):
        db.users.insert_one({
            "username": self.username,
            "email": self.email,
            "password": self.password
        })

class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = members

    def save(self):
        db.teams.insert_one({
            "name": self.name,
            "members": self.members
        })

class Activity:
    def __init__(self, user_id, activity_type, duration):
        self.user_id = user_id
        self.activity_type = activity_type
        self.duration = duration

    def save(self):
        db.activities.insert_one({
            "user_id": self.user_id,
            "activity_type": self.activity_type,
            "duration": self.duration
        })

class Leaderboard:
    def __init__(self, user_id, score):
        self.user_id = user_id
        self.score = score

    def save(self):
        db.leaderboards.insert_one({
            "user_id": self.user_id,
            "score": self.score
        })

class Workout:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def save(self):
        db.workouts.insert_one({
            "name": self.name,
            "description": self.description
        })
