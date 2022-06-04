from ..db import db


class UserInventory(db.Model):
    __tablename__ = "user_inventory"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ref_user: int = db.Column(
        db.BigInteger, db.ForeignKey("users.id"), index=True)
    ref_item: int = db.Column(
        db.Integer, db.ForeignKey("items.id"), index=True)
    qty: int = db.Column(db.Integer, server_default="0")
