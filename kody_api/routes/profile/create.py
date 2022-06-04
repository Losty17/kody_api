from werkzeug.exceptions import BadRequest
from sqlalchemy.exc import IntegrityError
from ...models import *
from .. import db
from ..blueprints import bp_profile
from flask_sqlalchemy import request as req


@bp_profile.get('/create')
def create_profile():
    params = {
        "id": req.headers.get('id'),
        "nickname": req.headers.get('nickname'),
        "bio": req.headers.get('bio'),
        "emoji": req.headers.get('emoji'),
        "featured_badge": req.headers.get('featured_badge'),
        "status": req.headers.get('status'),
    }
    if params['id'] and params['nickname']:
        u: User = User.query.filter_by(id=params['id']).one_or_none()

        if not u:
            u = User(params['id'])
            db.session.add(u)

        p: Profile = Profile(
            params['id'],
            params['nickname'],
            bio=params['bio'],
            emoji=params['emoji'],
            featured_badge=params['featured_badge'],
            status=params['status']
        )

        db.session.add(p)

        db.session.commit()
        return Profile.query.filter_by(ref_user=u.id).first().__dict__
    else:
        raise BadRequest()
