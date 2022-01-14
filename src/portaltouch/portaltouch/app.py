import os
import firebase_admin
from firebase_admin import credentials

from . import create_app
from .verify import verify_api

app = create_app()


@app.route('/')
def hello():
    return f'Hello, World! {app.config["SECRET_KEY"]}'


app.register_blueprint(verify_api)


filename = os.path.join(app.instance_path, "portaltouch-firebase.json")

cred = credentials.Certificate(filename)
firebase_app = firebase_admin.initialize_app(cred)
