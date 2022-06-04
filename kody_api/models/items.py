from ..db import db


class Item(db.Model):
    __tablename__ = "items"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(30), nullable=False)
    image: str = db.Column(db.String(100))
    emoji: str = db.Column(db.String(50))
    description: str = db.Column(db.String(80))
