import uuid
from flask import Flask, request

from .db import db


app = Flask(__name__)


@app.before_request
def handle_auth():
    # db.drop_all()
    # db.create_all()

    # token = request.headers.get('token')

    # if token != "placeholder":
    #     return {"error": "unauthorized"}, 401

    pass
