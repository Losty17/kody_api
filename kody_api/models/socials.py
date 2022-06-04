from ..db import db


class SocialType(db.Model):
    __tablename__ = "social_types"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(20), nullable=False)
    base_url: str = db.Column(db.String(50), nullable=False)
