from flask  import Blueprint, render_template, request, session, redirect, url_for

from .models import create_new_post, get_all_posts
from user.models import get_all_users

post = Blueprint(
    'post',
    __name__,
    url_prefix='/post',
    template_folder='templates'
)

@post.route("/compose", methods = ['POST'])
def compose(message = None):
    if session.get('logged_in'):
        content = request.form['compose-editor']
        username = session.get('username')
        create_new_post(content, username)
        return redirect(url_for('post.timeline'), code = 301)
    else:
        raise Exception("You should login first!")


@post.route("/timeline", methods = ['GET'])
def timeline():
    posts = get_all_posts()
    users = get_all_users()
    return render_template(
        'timeline.html',
        posts = posts,
        users = users
    )