from flask import Flask, make_response, jsonify, session, flash, \
                  get_flashed_messages, request

app = Flask(__name__)
app.config.from_pyfile('config.py')

from . import a, b, api
app.register_blueprint(a.bp, url_prefix='/a')
app.register_blueprint(b.bp, url_prefix='/b')
app.register_blueprint(api.bp, subdomain='api')


@app.route('/')
def index():
    flash('index')
    return 'index'


@app.route('/1')
def one():
    flash('1')
    list_comprehension = [i for i in range(10)]
    return jsonify(
                    okboomer='1',
                    spaceindent='yess',
                    no='no'
        )
    return jsonify(list_comprehension)


@app.route('/2')
def two():
    flash('2')
    if 'one' in session:
        return 'found session'
    else:
        return 'no session'


@app.route('/2/a')
def two_session_create():
    session['one'] = 1
    return 'session succed'


@app.route('/2/b')
def two_session_delete():
    session.pop('one', None)
    return 'session pop!'


@app.route('/3')
def three():
    print(get_flashed_messages())
    return jsonify(get_flashed_messages())
    return 'hi'
    return get_flashed_messages()


@app.route('/4/a')
def four_set_cookie():
    if request.cookies.get('cookietest'):
        print('we got cookie!')
        return 'alrdy got cokie'
    resp = make_response('cookie set')
    resp.set_cookie('cookietest', 'abc', 10)
    return resp


@app.route('/4')
def four_read_cookie():
    return request.cookies


@app.route('/5/<irst>/<second>')
def five_url_stuff(irst, second):
    return irst + second


@app.route('/6')
def six():
    return '6'


from flask.views import View
class ShowUsers(View):
    def dispatch_request(self):
        return 'hello!'
app.add_url_rule('/6/a', view_func=ShowUsers.as_view('show_users'))


@app.errorhandler(404)
def page_not_found(error):
    my_dict = {
        'one': 'Value one',
        'two': 'Value two',
        'three': 'Value three',
        'four': 'Value four',
    }
    resp = make_response(my_dict, 404)
    resp.headers['Custom-Header'] = 'hello word'
    
    return resp


@app.errorhandler(401)
def unauthorized(error):
    return 'page not authorized'
