from flask import Flask
from flask_pymongo import PyMongo
from flask_login import LoginManager
from os import path

mongo = PyMongo()
db = None

def create_app(secret_key, db_uri):
    global db

    app = Flask(__name__)
    app.config["SECRET_KEY"] = secret_key
    app.config["MONGO_URI"] = db_uri

    mongo.init_app(app)
    db = mongo.db

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    
    @login_manager.user_loader
    def load_user(user_id):
        from .models import User
        from bson.objectid import ObjectId

        user = db.users.find_one(filter={"_id" : user_id})
        return User.conv_to_obj(user) if user else None

    return app