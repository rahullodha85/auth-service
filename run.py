from app import app
from app.routes.authenticate import authenticate

app.register_blueprint(authenticate, url_prefix='/authenticate')


@app.route('/')
def index():
    return 'Home Page!'


if __name__ == '__main__':
    app.run(host=app.config.get('HOST'), port=app.config.get('PORT'))
