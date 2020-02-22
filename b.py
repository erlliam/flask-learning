from flask import Blueprint, session, current_app
from functools import wraps

bp = Blueprint('b', __name__, url_prefix='/b')


def decorated_test(f):
    @wraps(f)
    def wrapper():
        if 'one' in session:
            result = f()
            return result
        else:
            return 'no session'
    return wrapper

@bp.route('/deco_test')
@decorated_test
def test_deco():
    print(current_app)
    return 'welcome to /b/'

@bp.route('/')
def index():
    print(current_app)
    return 'welcome to /b/'

