from flask.blueprints import Blueprint
from flask import current_app, render_template, request

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("portaltouch-firebase.json")
firebase_admin.initialize_app(cred)

verify_api = Blueprint('verify-api', __name__, url_prefix='/verify')


@verify_api.route('/login')
def verify_login():
    return render_template('login.html')


@verify_api.post('/phone')
def verify_phone():
    param = request.values["phone"]
    return f'Hello, World! {param}'


@verify_api.route('/code')
def verify_code():
    return 'Hello, World!'
