from flask import Flask, render_template
from app.config import config_obj
from app.db import connect_to_db
from app.puzzles import PuzzlesService

# App config
static_folder = '../../client/dist/assets'
template_folder = '../../client/dist'
app = Flask(__name__, static_url_path='', static_folder=static_folder, template_folder=template_folder)
app.config.from_object(config_obj)

# Database config
DB_URI = app.config['DB_URI']
db_connection = connect_to_db(DB_URI)

puzzles_service = PuzzlesService(db_connection)

# Routes
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/puzzles")
def get_puzzles():
    puzzles = puzzles_service.find()
    return puzzles