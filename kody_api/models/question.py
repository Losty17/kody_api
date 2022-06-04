from ..db import db


class Question(db.Model):
    __tablename__ = "questions"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ref_node: int = db.Column(
        db.Integer, db.ForeignKey("nodes.id"), index=True)
    text: str = db.Column(db.String(200), nullable=False)
    explanation: str = db.Column(db.String(200))
    right_ans: str = db.Column(db.String(50), nullable=False)
    fst_ans: str = db.Column(db.String(50), nullable=False)
    snd_ans: str = db.Column(db.String(50))
    thd_ans: str = db.Column(db.String(50))
