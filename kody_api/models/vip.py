from ..db import db


class Vip(db.Model):
    __tablename__ = "vips"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(4), nullable=False)
    image: str = db.Column(db.String(100))
    emoji: str = db.Column(db.String(50))
    description: str = db.Column(db.String(80))
