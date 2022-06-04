from werkzeug.exceptions import NotFound
from sqlalchemy import func

from ...models import Question
from ..blueprints import bp_question as q


@q.get('/random')
def get_random_question() -> Question:
    q = Question.query\
        .order_by(func.random())\
        .limit(1)\
        .one_or_none()

    if q:
        return q.__dict__
    else:
        raise NotFound()
