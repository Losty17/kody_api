from flask import Blueprint, request
from sqlalchemy.engine.row import Row
from werkzeug.exceptions import NotFound, BadRequest

from ...models import *
from ...utils import row_to_json
from .. import db
from ..blueprints import bp_user


@bp_user.get('/')
def get_user():
    d = request.get_json()
    if type(d) is dict and 'id' in d:
        u: User = User.query.filter_by(id=d['id']).first()

        if u:
            return u.__dict__

        else:
            raise NotFound()

    else:
        return BadRequest()


@bp_user.post('/create')
def create_user():
    d = request.get_json()
    if type(d) is dict and 'id' in d:
        u = User(d['id'])

        db.session.add(u)
        db.session.commit()

        return User.query.filter_by(id=d['id']).first().__dict__

    else:
        raise BadRequest()
