from typing import List

from flask import Blueprint, request
from sqlalchemy.engine.row import Row

from ..models import *
from ..utils import row_to_json
from . import app, db

user = Blueprint('user', __name__, url_prefix='/user')


@user.get('/<int:_id>')
def get_user(_id: int):
    u: User = User.query.filter_by(id=_id).first()

    return u.__dict__ if u else {"error": "user not found"}, 404


@user.get('/<int:_id>/profile')
def get_profile(_id: int):
    profile: Row = Profile.query\
        .join(User, User.id == Profile.ref_user)\
        .add_columns(User.id, User.ref_vip, User.streak, User.dt_created)\
        .filter(User.id == Profile.ref_user)\
        .filter(User.id == _id)\
        .first()

    return row_to_json(profile)


@user.post('/user')
def create_user():
    _id = int(request.headers['id'])
    u = User(_id)

    db.session.add(u)
    db.session.commit()

    return User.query.filter_by(id=_id).first().to_json()


@user.get('/create/<int:_id>/profile')
def create_profile(_id: int):
    p = Profile(_id, 'losty')

    db.session.add(p)
    db.session.commit()

    return "ok"
