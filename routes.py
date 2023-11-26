 from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    me = {
        "first_name": "Jesenia",
        "last_name": "Guerrero",
        "hobbies": "coding",
        "is_active": True
    }
    return me