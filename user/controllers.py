from flask  import Blueprint, render_template, request, session, redirect, url_for

from .models import valid_login, username_or_email_taken, create_new_user, get_user_profile

user = Blueprint(
    'user',
    __name__,
    url_prefix='/user',
    template_folder='templates'
)

@user.route("/signup", methods = ['POST', 'GET'])
def signup(message = None):
    fields = [
        {
            'name': 'firstname',
            'type': 'text'
        },
        {
            'name': 'lastname',
            'type': 'text'
        },
        {
            'name': 'username',
            'type': 'text'
        },
        {
            'name': 'email',
            'type': 'email'
        },
        {
            'name': 'password',
            'type': 'password'
        }
    ]
    if request.method == 'POST':
        if not username_or_email_taken(
            request.form['username'],
            request.form['email']
        ):
            create_new_user(
                request.form
            )
            return redirect(url_for('user.signin'), code = 301)
        else:
            message = "email or username is taken."
    return render_template(
        'signup.html',
        fields = fields,
        message = message
    )

@user.route("/signin", methods = ['POST', 'GET'])
def signin(message = None):
    fields = [
        {
            'name': 'username',
            'type': 'text'
        },
        {
            'name': 'password',
            'type': 'password'
        }
    ]
    if request.method == 'POST':
        if valid_login(
                request.form['username'],
                request.form['password']
            ):
            session['logged_in'] = True
            session['username'] = request.form['username']
            return redirect(url_for('post.timeline'), code = 301)
        else:
            message = "Invalid username or password"
    return render_template(
        'signin.html',
        fields = fields,
        message = message
    )

@user.route("/signout", methods = ['GET'])
def signout():
    if session.get('logged_in'):
        session['logged_in'] = False
    return signin('Sign Out Succesfully!')

@user.route('/profile', methods = ['GET'])
def profile():
    username = session.get('username')
    fields = []
    if username:
        fields = get_user_profile(username)
    return render_template(
        'profile.html',
        fields = fields
    )