import os
from peewee import *
from playhouse.db_url import connect

mysql_db = connect(os.environ.get("DATABASE_URI") or "mysql://root:1234@localhost:3306/test_db")

class BaseModel(Model): #Mysql Database Base Model Class
    """A base model that will use our MySQL database"""
    class Meta:
        database = mysql_db