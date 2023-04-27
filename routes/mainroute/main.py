from flask import Blueprint, session

MainRoute = Blueprint("MainRoute", __name__)

@MainRoute.route("/")
def User():
    return "<p>Hello</p>"

@MainRoute.route("/help")
def Help():
    return "<p>Help</p>"