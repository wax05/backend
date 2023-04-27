from flask import Blueprint, session
from models.userdata import UserData

AdminRoute = Blueprint("AdminRoute", __name__)

@AdminRoute.route("/user/<string:name>", methods=["GET","POST"])
def User(name:str):
    return "Done"

        