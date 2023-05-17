"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7pnu4dadc9vlvt840-a.oregon-postgres.render.com",
        database="todo_4zjs",
        user="root",
        password="daXw7lY4sGvEtFYfTMVRUeEN9WS9Owes")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
