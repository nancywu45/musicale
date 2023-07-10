from flask import Blueprint, render_template

home_blueprint: Blueprint = Blueprint("home_bp", __name__)


@home_blueprint.route("/", methods=["GET"])
def home() -> str:
    return render_template("home/home.html")
