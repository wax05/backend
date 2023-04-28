from peewee import *
from utils.orm.base import BaseModel

class UserData(BaseModel):
    UseriD = CharField(20)
    name = CharField(10)