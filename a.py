from flask import Blueprint

bp = Blueprint('a', __name__)

@bp.url_value_preprocessor
def what(endpoint, values):
    print(endpoint, values)
    test = values.pop('ok', None)

@bp.url_defaults
def default(endpoint, values):
    print('hold up')
    

@bp.route('/')
def index():
    return 'welcome to /a/'
@bp.route('/<ok>')
def values_test():
    return 'welcome to values test'
@bp.route('/login')
def login():
    return 'welcome to /a/login'
