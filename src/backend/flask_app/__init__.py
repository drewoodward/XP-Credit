from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('flask_app.config.Config')

    # Import and register blueprints or routes
    from flask_app.routes import main
    app.register_blueprint(main)

    return app
