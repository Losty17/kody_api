from ..db import db


class UserBadge(db.Model):
    __tablename__ = "user_badges"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ref_user: int = db.Column(
        db.BigInteger, db.ForeignKey("users.id"), index=True)
    ref_badge: int = db.Column(
        db.Integer, db.ForeignKey("badges.id"), index=True)

    __table_args__ = (
        db.UniqueConstraint('ref_user', 'ref_badge', name='u_user_badge'),
    )
