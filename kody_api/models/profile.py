from ..db import db


class Profile(db.Model):
    __tablename__ = "user_profiles"
    __dict__ = {}

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ref_user: int = db.Column(
        db.BigInteger, db.ForeignKey("users.id"), index=True, unique=True)
    featured_badge: int = db.Column(db.Integer, db.ForeignKey("badges.id"))
    nickname: str = db.Column(db.String(30), nullable=False)
    bio: str = db.Column(db.String(200))
    status: str = db.Column(db.String(50))
    emoji: str = db.Column(db.String(50))

    def __init__(self, user_id: int, nickname: str, **kwargs) -> None:
        super().__init__(ref_user=user_id, nickname=nickname, **kwargs)

    def __repr__(self) -> str:
        return f"<Profile user={self.ref_user} name={self.nickname}>"
