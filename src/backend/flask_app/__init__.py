from flask import Flask
from flask_app.firestore_listener import start_listener_in_background  # Import the listener function

def create_app():
    app = Flask(__name__)
    app.config.from_object('flask_app.config.Config')

    # Start Firestore real-time listener in a background thread
    start_listener_in_background()

    # Import and register blueprints or routes
    from flask_app.routes import main
    app.register_blueprint(main)

    return app
