from .app import app
from .db import db
from .routes import *

app.register_blueprint(user)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///testes.db"
app.config['SQLALCHEMY_BINDS'] = {}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
