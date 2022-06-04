from ..db import db


class UserBit(db.Model):
    __tablename__ = "user_bits"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ref_user: int = db.Column(
        db.BigInteger, db.ForeignKey("users.id"), index=True)
    ref_node: int = db.Column(
        db.Integer, db.ForeignKey("nodes.id"), index=True)
    qty: int = db.Column(db.Integer, server_default="0")
