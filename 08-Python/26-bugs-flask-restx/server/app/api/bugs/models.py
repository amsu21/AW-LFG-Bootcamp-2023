import datetime
from app import db

class Bug(db.Model):
    __tablename__ = "bugs"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    is_closed = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.today())
    

    