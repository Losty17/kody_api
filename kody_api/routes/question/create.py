from tkinter import N
from typing import List

from flask import request
from werkzeug.exceptions import BadRequest

from ...db import db
from ...models import Question
from ...utils import check_question_data
from ..blueprints import bp_question as q


@q.post('/add')
def create_question():
    data = request.get_json()

    if type(data) is dict:
        q = check_question_data(data)

        if q:
            db.session.add(q)
            db.session.commit()

            return {"message": "added 1 question"}, 200

        else:
            raise BadRequest()

    else:
        raise BadRequest()


@q.post('/add/multiple')
def create_questions():
    data = request.get_json()

    if type(data) is list:
        q: List[Question] = []
        counter = 0
        for d in data:
            question = check_question_data(d)

            if question:
                q.append(question)
                counter += 1

        db.session.bulk_save_objects(q)
        db.session.commit()

        return {"message": f"added {counter} questions"}, 200

    else:
        raise BadRequest()
