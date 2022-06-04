from .app import app
from .db import db
from .routes import *
from .handlers import *

app.register_blueprint(bp_user)
app.register_blueprint(bp_profile)
app.register_blueprint(bp_question)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///testes.db"
app.config['SQLALCHEMY_BINDS'] = {}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
