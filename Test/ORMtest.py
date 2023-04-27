from utils.orm.base import mysql_db as db
from utils.orm.model import UserData

def Test():
    db.connect()
    db.create_tables([UserData])
    insertData = UserData(UseriD = "Test1", name = "Test123")
    insertData1 = UserData(UseriD = "Test2", name = "Test1234")
    if insertData.save() and insertData1.save() != 1:
        return "ERROR"