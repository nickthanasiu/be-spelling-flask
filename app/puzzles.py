from bson import json_util

class PuzzlesService:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def find(self, *args, **kwargs):
        puzzles_cursor = self.db_connection.puzzles.find(*args, **kwargs)
        return json_util.dumps(puzzles_cursor)