from ..db import db


class UserSocial(db.Model):
    __tablename__ = "user_socials"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ref_user: int = db.Column(
        db.BigInteger, db.ForeignKey("users.id"), index=True)
    ref_social_type: int = db.Column(
        db.Integer, db.ForeignKey("social_types.id"))
    username: str = db.Column(db.String(20), nullable=False)
