from flask_session import Session
from flask_wtf import CSRFProtect 
from flask import Flask, redirect, request, url_for,render_template
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from decouple import config
from dotenv import load_dotenv,dotenv_values

app=Flask(__name__)
load_dotenv()
app.config.from_object(config("APP_SETTINGS"))
app.config['SECRET_KEY'] = 'your_secret_key'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
# login_manager = LoginManager(app)
# login_manager.init_app(app)
Session(app)
CSRFProtect(app) 


with app.app_context():
    from core.views import core_bp
    app.register_blueprint(core_bp)