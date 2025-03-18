from flask import Flask
from flask_cors import CORS  # Import CORS
from flask_app.firestore_listener import start_listener_in_background  # Import Firestore listener

def create_app():
    app = Flask(__name__)
    app.config.from_object('flask_app.config.Config')

    # Enable CORS to allow frontend to access backend
    CORS(app)

    # Start Firestore real-time listener in a background thread
    start_listener_in_background()

    # Import and register blueprints or routes
    from flask_app.routes import main
    app.register_blueprint(main)

    return app
