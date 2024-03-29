import os

from flask import Flask
from headers import set_response_headers

dir_path = os.path.dirname(os.path.realpath(__file__))

db_path = os.path.join(dir_path, "sqlite3.db")

app = Flask(__name__)
app.secret_key = "c287c9e3e30f43e3bdd1161625ae3318"
app.after_request(set_response_headers)

@app.route('/ping')
def ping():
    return "pong"

from user.controllers import user as user_app  # noqa: E402
from post.controllers import post as post_app  # noqa: E402

app.register_blueprint(user_app)
app.register_blueprint(post_app)