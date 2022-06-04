from datetime import datetime
from ..db import db
from sqlalchemy.sql import func


class User(db.Model):
    __tablename__ = "users"
    __dict__ = {}

    id: int = db.Column(db.BigInteger, primary_key=True, nullable=False)
    ref_vip: int = db.Column(db.Integer, db.ForeignKey(
        "vips.id"), index=True, server_default='0')

    streak: int = db.Column(db.Integer, server_default="0")
    last_vote: datetime = db.Column(db.DateTime)
    last_daily: datetime = db.Column(db.DateTime)
    last_question: datetime = db.Column(db.DateTime)

    dt_created: datetime = db.Column(
        db.DateTime, server_default=func.now())

    def __init__(self, _id: int) -> None:
        super(User, self).__init__(id=_id)

    def __repr__(self) -> str:
        return f"<User id={self.id}>"
