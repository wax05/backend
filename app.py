from flask import Flask
from extension import db
from routes.admin import AdminRoute
from routes.main import MainRoute
def Create_App():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"#
    app.register_blueprint(MainRoute)
    app.register_blueprint(AdminRoute)
    db.init_app(app)

    @app.before_first_request#Sqlite3 Sql Table Init
    def create_database():
        db.create_all()
    return app

if __name__ == "__main__":
    Create_App().run(debug=True)#DEV Only