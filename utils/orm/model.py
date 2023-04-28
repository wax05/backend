from peewee import *
from base import BaseModel

class UserData(BaseModel):
    UseriD = CharField(20)
    name = CharField(10)