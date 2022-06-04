from flask import Blueprint


bp_user = Blueprint('user', __name__, url_prefix='/user')
bp_profile = Blueprint('profile', __name__, url_prefix='/profile')
bp_question = Blueprint('question', __name__, url_prefix='/question')
