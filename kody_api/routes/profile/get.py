from flask import request as req
from werkzeug.exceptions import BadRequest, NotFound

from ...models import *
from ...utils import row_to_json
from ..blueprints import bp_profile


@bp_profile.get('/')
def get_profile():
    data = req.get_json()
    if type(data) is dict and "id" in data:
        p = Profile.query\
            .join(User, User.id == Profile.ref_user)\
            .add_columns(User.ref_vip, User.streak, User.dt_created)\
            .filter(User.id == data['id'])\
            .first()
        # .filter(User.id == Profile.ref_user)\

        if p:
            return row_to_json(p)

        else:
            raise NotFound()
    else:
        raise BadRequest()
