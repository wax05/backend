from flask import Blueprint

AdminRoute = Blueprint("AdminRoute", __name__)

@AdminRoute.route("/user/<string:name>", methods=["GET","POST"])
def User(name:str):
    return "Done"

        