from extension import db
import sqlalchemy as sa

class sessions(db.Model):
    UUID = db.Column(db.String(36), primary_key=True)
    Id = db.Column(sa.ForeignKey("UserData.Id"))