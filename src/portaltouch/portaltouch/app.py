from . import create_app
from .verify import verify_api

app = create_app()


@app.route('/')
def hello():
    return 'Hello, World!'


app.register_blueprint(verify_api)
