from flask.blueprints import Blueprint
from flask import current_app, render_template, request
from firebase_admin.auth import verify_id_token

verify_api = Blueprint('verify-api', __name__, url_prefix='/verify')

# export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1
# export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1
#  for install firebase-admin


@verify_api.route('/login')
def verify_login():
    return render_template('login.html',
                           liff_id=current_app.config["LIFF_ID"],
                           api_key=current_app.config["FIREBASE_API_KEY"])


@ verify_api.post('/phone')
def verify_phone():
    param = request.values["phone"]
    return f'Hello, World! {param}'


@ verify_api.route('/code')
def verify_code():
    param = request.values["token"]
    line_id = request.values["line_id"]

    result = verify_id_token(param).get("uid", '')

    # send a message to line user

    if line_id:
        pass

    return f'Hello, World! {result}'
