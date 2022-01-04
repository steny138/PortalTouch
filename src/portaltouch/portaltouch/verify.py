import os
from flask.blueprints import Blueprint
from flask import current_app, render_template, request
from firebase_admin.auth import create_custom_token

verify_api = Blueprint('verify-api', __name__, url_prefix='/verify')

# export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1
# export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1
#  for install firebase-admin


@verify_api.route('/login')
def verify_login():
    return render_template('login.html',
                           liff_id=current_app.config["LIFF_ID"])


@ verify_api.post('/phone')
def verify_phone():
    param = request.values["phone"]
    return f'Hello, World! {param}'


@ verify_api.route('/code')
def verify_code():
    param = request.values["token"]
    return f'Hello, World! {param}'
