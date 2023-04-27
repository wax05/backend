from flask import Blueprint, request, make_response

TestRoute = Blueprint("TestRoute", __name__)

@TestRoute.route("/session/make")
def Test():
    resp = make_response()
    resp.set_cookie('username', 'the username')
    return 

@TestRoute.route("/session/check")
def SessionCheck():
    SessionKey = request.cookies.get("SessionKey")
    return SessionKey