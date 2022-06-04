from flask import Blueprint, request
from sqlalchemy.engine.row import Row

from ...models import *
from ...utils import row_to_json
from .. import db
from ..blueprints import bp_user


@bp_user.get('/<int:_id>')
def get_user(_id: int):
    u: User = User.query.filter_by(id=_id).first()

    return u.__dict__ if u else {"error": "user not found"}, 404


@bp_user.get('/<int:_id>/profile')
def get_profile(_id: int):
    profile: Row = Profile.query\
        .join(User, User.id == Profile.ref_user)\
        .add_columns(User.id, User.ref_vip, User.streak, User.dt_created)\
        .filter(User.id == Profile.ref_user)\
        .filter(User.id == _id)\
        .first()

    return row_to_json(profile) or {"error": "profile not found"}, 404


@bp_user.post('/create')
def create_user():
    _id = int(request.headers.get('id'))
    u = User(_id)

    db.session.add(u)
    db.session.commit()

    return User.query.filter_by(id=_id).first().__dict__
