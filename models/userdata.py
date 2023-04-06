from extension import db
class UserData(db.Model):
    Id = db.Column(db.String(20), primary_key=True)
    Name = db.Column(db.String(10))
    Email = db.Column(db.String(80))
    UserClass = db.Column(db.String(20))