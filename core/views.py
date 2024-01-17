from flask import Blueprint, render_template,redirect,url_for,session,flash
from flask_login import login_required, current_user

core_bp = Blueprint("core", __name__)

@core_bp.route("/")
def homepage():
    return render_template("core/homepage.html")