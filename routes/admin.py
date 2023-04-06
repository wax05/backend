from flask import Blueprint
from models.userdata import UserData
from extension import db

AdminRoute = Blueprint("AdminRoute", __name__)

@AdminRoute.route("/user/<string:name>", methods=["GET","POST"])
def User(name:str):
    user = UserData(Id=name,Name="hi",Email="example@example.com",UserClass="Admin")
    db.session.add(user)
    db.session.commit()
    return "Done"