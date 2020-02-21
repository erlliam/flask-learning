from flask import Blueprint, url_for, redirect, abort, Response

bp = Blueprint('api', __name__)


@bp.url_defaults
def add_language_code(endpoint, values):
    print('executed')
    print(endpoint, values)

@bp.url_value_preprocessor
def test(e, v):
    pass


@bp.route('/')
def index():
    return 'api index'

@bp.route('/reroute')
def reroute():
    abort(Response('hi?'))
    abort(404)
    return redirect(url_for('.hello_with_test', test='123'))

@bp.route('/hello')
def hello():
    return 'Hello. This subdomain thing is pretty awesome.'

@bp.route('/hello/<test>')
def hello_with_test(test):
    return 'Hello. This subdomain thing is pretty awesome.'
