from flask import Flask
from app.config import config_obj
from app.db import connect_to_db
from app.puzzles import PuzzlesService

# App config
app = Flask(__name__)
app.config.from_object(config_obj)

# Database config
DB_URI = app.config['DB_URI']
db_connection = connect_to_db(DB_URI)

# Routes
@app.route("/")
def index():
    return '<h1>Be Spelling</h1>'

puzzles_service = PuzzlesService(db_connection)

@app.route("/puzzles")
def get_puzzles():
    puzzles = puzzles_service.find()
    return puzzles