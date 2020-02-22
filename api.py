from flask import Blueprint, url_for, redirect, abort, Response
from flask.views import View

bp = Blueprint('api', __name__)

@bp.url_defaults
def add_language_code(endpoint, values):
    print('executed')
    print(endpoint, values)

@bp.url_value_preprocessor
def test(e, v):
    pass



class CustomView(View):
    def dispatch_request(self):
        return 'view as a class wtf? useles!'

bp.add_url_rule('/wtf', view_func=CustomView.as_view('customview'))





@bp.route('/')
def index():
    return url_for('.reroute')

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

@bp.route('/ok/', defaults={'page': 'index'})
@bp.route('/ok/<page>')
def show(page):
    return page
