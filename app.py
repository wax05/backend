import sys
from flask import Flask
from routes.adminroute.admin import AdminRoute
from routes.mainroute.main import MainRoute
from config import config
from utils.orm.db_init import db_init

app = Flask(__name__)
app.config.from_object(config.TestConfig)
app.register_blueprint(MainRoute)
app.register_blueprint(AdminRoute,url_prefix="/admin")
if not db_init():
    sys.exit("Db Table is not Initialized")

if __name__ == "__main__":
    app.run(debug=True)#DEV Only

