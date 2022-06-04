from ..models import NODE_IDS, Question


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
