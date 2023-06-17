from flask import Flask


# __name__ is package
app=Flask(__name__) 
 
#  route is the decorator
@app.route("/")
def hello_world():
    return "<p>hello world go code ans  <p>"
@app.route("/blog")
def blog():
    return "<h1> blog page</h1>"

# add variable
from markupsafe import escape
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath{escape(subpath)}'

from flask import url_for

# @app.route('/')
# def index():
#     return 'index'

# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))


# from flask import request

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()
    
# @app.get('/login')
# def login_get():
#     return show_the_login_form()

# @app.post('/login')
# def login_post():
#     return do_the_login() 


# url_for('static',filename='style.css')

from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)