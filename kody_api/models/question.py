from ..db import db


class Question(db.Model):
    __tablename__ = "questions"
    __dict__ = {}

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ref_node: int = db.Column(
        db.Integer, db.ForeignKey("nodes.id"), index=True, nullable=False)
    text: str = db.Column(db.String(200), nullable=False)
    explanation: str = db.Column(db.String(200))
    right_ans: str = db.Column(db.String(50), nullable=False)
    fst_ans: str = db.Column(db.String(50), nullable=False)
    snd_ans: str = db.Column(db.String(50))
    thd_ans: str = db.Column(db.String(50))

    def __init__(self, text: str, node: int, right_ans: str, fst_ans: str, **kwargs) -> None:
        super().__init__(
            text=text,
            ref_node=node,
            right_ans=right_ans,
            fst_ans=fst_ans,
            **kwargs
        )
