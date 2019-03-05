from flask  import Blueprint, render_template, request, session, redirect, url_for

from .models import create_new_post, get_all_posts

post = Blueprint(
    'post',
    __name__,
    url_prefix='/post',
    template_folder='templates'
)

@post.route("/compose", methods = ['POST', 'GET'])
def compose(message = None):
    fields = [
        {
            'name': 'content',
            'placeholder': 'What\'s in your mind?'
        }
    ]
    if request.method == 'POST':
        if session.get('logged_in'):
            content = request.form['content']
            username = session.get('username')
            create_new_post(content, username)
            return redirect(url_for('post.timeline'), code = 301)
        else:
            message = "You should login first!"
    return render_template(
        'compose.html',
        fields = fields,
        message = message
    )


@post.route("/timeline", methods = ['GET'])
def timeline():
    posts = get_all_posts()
    return render_template(
        'timeline.html',
        posts = posts
    )