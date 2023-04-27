from flask import Flask
from routes.adminroute.admin import AdminRoute
from routes.mainroute.main import MainRoute
from config import config
def Create_App():
    app = Flask(__name__)
    app.config.from_object(config.TestConfig)
    app.register_blueprint(MainRoute)
    app.register_blueprint(AdminRoute,url_prefix="/admin")
    return app

if __name__ == "__main__":
    Create_App().run(debug=True)#DEV Only