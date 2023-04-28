from utils.orm import base, model

def db_init()->bool:
    try:
        db = base.db
        db.connect()
        db.create_tables([model.UserData])
        return True
    except:
        return False
