import uuid
from flask import Flask, request


app = Flask(__name__)


@app.before_request
def handle_auth():
    token = request.headers.get('token')

    if token != "placeholder":
        return {"error": "unauthorized"}, 401
