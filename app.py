import pyrebase
import json

with open("auth.json") as f:
    config = json.load(f)

firebase = pyrebase.initialize_app(config)
db = firebase.database()

signin = {"password":"result_by_hash(pw)", "username":"TaeHyeok"}
db.child("users").child("hth021002").set(signin)