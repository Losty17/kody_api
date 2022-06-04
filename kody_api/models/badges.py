from ..db import db


class Badge(db.Model):
    __tablename__ = "badges"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(30), nullable=False)
    image: str = db.Column(db.String(100))
    emoji: str = db.Column(db.String(50))
