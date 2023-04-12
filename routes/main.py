from flask import Blueprint

MainRoute = Blueprint("MainRoute", __name__)

@MainRoute.route("/")
def User():
    return "<p>Hello</p>"