from datetime import datetime
from typing import Any, Dict
from ..db import db
from sqlalchemy.sql import func


class Vip(db.Model):
    __tablename__ = "vips"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(4), nullable=False)
    image: str = db.Column(db.String(100))
    emoji: str = db.Column(db.String(50))
    description: str = db.Column(db.String(80))


class Node(db.Model):
    __tablename__ = "nodes"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(8), nullable=False)
    image: str = db.Column(db.String(100))
    emoji: str = db.Column(db.String(50))
    description: str = db.Column(db.String(80))


class User(db.Model):
    __tablename__ = "users"
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

    def to_json(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'vip': self.ref_vip,
            'streak': self.streak,
            'last_vote': self.last_vote,
            'last_question': self.last_question,
            'last_daily': self.last_daily,
            'dt_created': self.dt_created,
        }


class UserBit(db.Model):
    __tablename__ = "user_bits"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ref_user: int = db.Column(
        db.BigInteger, db.ForeignKey("users.id"), index=True)
    ref_node: int = db.Column(
        db.Integer, db.ForeignKey("nodes.id"), index=True)
    qty: int = db.Column(db.Integer, server_default="0")


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


class Item(db.Model):
    __tablename__ = "items"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(30), nullable=False)
    image: str = db.Column(db.String(100))
    emoji: str = db.Column(db.String(50))
    description: str = db.Column(db.String(80))


class UserInventory(db.Model):
    __tablename__ = "user_inventory"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ref_user: int = db.Column(
        db.BigInteger, db.ForeignKey("users.id"), index=True)
    ref_item: int = db.Column(
        db.Integer, db.ForeignKey("items.id"), index=True)
    qty: int = db.Column(db.Integer, server_default="0")


class Badge(db.Model):
    __tablename__ = "badges"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(30), nullable=False)
    image: str = db.Column(db.String(100))
    emoji: str = db.Column(db.String(50))


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


class SocialType(db.Model):
    __tablename__ = "social_types"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(20), nullable=False)
    base_url: str = db.Column(db.String(50), nullable=False)


class UserSocial(db.Model):
    __tablename__ = "user_socials"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ref_user: int = db.Column(
        db.BigInteger, db.ForeignKey("users.id"), index=True)
    ref_social_type: int = db.Column(
        db.Integer, db.ForeignKey("social_types.id"))
    username: str = db.Column(db.String(20), nullable=False)


class UserProfile(db.Model):
    __tablename__ = "user_profiles"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ref_user: int = db.Column(
        db.BigInteger, db.ForeignKey("users.id"), index=True)
    featured_badge: int = db.Column(db.Integer, db.ForeignKey("badges.id"))
    nickname: str = db.Column(db.String(30), nullable=False)
    bio: str = db.Column(db.String(200))
    status: str = db.Column(db.String(50))
    emoji: str = db.Column(db.String(50))
