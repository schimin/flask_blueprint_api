from flask import Flask


def create_app():
    app = Flask(__name__)

    from api.route.home import home_api
    app.register_blueprint(home_api, url_prefix='/api')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5051)
