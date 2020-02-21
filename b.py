from flask import Blueprint

bp = Blueprint('b', __name__, url_prefix='/b')

@bp.route('/')
def index():
    return 'welcome to /b/'
