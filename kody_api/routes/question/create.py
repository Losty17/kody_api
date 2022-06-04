from tkinter import N
from typing import List

from flask import request
from sqlalchemy import func
from werkzeug.exceptions import NotFound, BadRequest

from ...db import db
from ...models import NODE_IDS, Question
from ..blueprints import bp_question as q


def check_question_data(d) -> Question | None:
    try:
        question = Question(
            d['text'],
            NODE_IDS[d['node']],
            d['right_ans'],
            d['fst_ans'],
        )

        question.snd_ans = d['snd_ans'] if 'snd_ans' in d else None
        question.thd_ans = d['thd_ans'] if 'thd_ans' in d else None
        question.explanation = d['explanation'] if 'explanation' in d else None

    except:
        return None

    else:
        return question


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
