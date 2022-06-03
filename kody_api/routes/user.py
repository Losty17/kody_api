from flask import request
from . import app, db
from ..models import *


@app.get("/user/<int:_id>")
def get_user(_id: int):
    u: User = User.query.filter_by(id=_id).first()

    return u.to_json() if u else {"error": "user not found"}, 404


@app.post('/user')
def create_user():
    _id = int(request.headers['id'])
    u = User(_id)

    db.session.add(u)
    db.session.commit()

    return User.query.filter_by(id=_id).first().to_json()
