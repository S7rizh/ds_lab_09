from flask import Flask, render_template, request, redirect, escape
from pymongo import MongoClient, DESCENDING
import json
import datetime

app = Flask(__name__)

DB_CREDENTIALS_FILE = "db_credentials.json"
MAX_MESSAGES = 20

def init_database():
    with open(DB_CREDENTIALS_FILE) as cred_file:
        db_credentials = json.load(cred_file)

    # db_client = MongoClient("mongodb+srv://{username}:{password}@cluster0-bor6t.mongodb.net/test?retryWrites=true&w=majority".format(**db_credentials))
    db_client = MongoClient(db_credentials['server'], replicaset=db_credentials['replicaset'], connect=False)
    return db_client

def add_message_to_db(username, message):
    new_post = {
        'username' : escape(username),
        'message' : escape(message),
        'time' : datetime.datetime.today()
    }
    db.messages.insert_one(new_post)

def populate_db():
    add_message_to_db(**{"username" : "Adele", "message" : "Hello from the other side"})
    add_message_to_db(**{"username" : "Adele", "message" : "I must've called a thousand times"})
    add_message_to_db(**{"username" : "Adele", "message" : "To tell you I'm sorry"})
    add_message_to_db(**{"username" : "Adele", "message" : "For everything that I've done"})
    add_message_to_db(**{"username" : "Adele", "message" : "But when I call you never"})
    add_message_to_db(**{"username" : "Adele", "message" : "Seem to be home"})
    add_message_to_db(**{"username" : "Someone", "message" : "Wow, what is Adele doing in this chat? :D"})

# Initialization

db_client = init_database()
db = db_client.test
populate_db()

# Routes

@app.route('/', methods=("GET",))
def chat_page():
    if request.method == "GET":
        posted_messages = []
        for post in db.messages.find().sort("time", DESCENDING).limit(MAX_MESSAGES):
            posted_messages.append(post)
        return render_template("index.html", posted_messages=posted_messages)

@app.route("/post_message", methods=("POST",))
def post_message():
    if request.method == "POST":
        username = request.form['username']
        message = request.form['message']
        add_message_to_db(username, message)
        return redirect("/")

