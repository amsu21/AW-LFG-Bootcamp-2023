from db import db
from datetime import datetime

class ProjectModel(db.Model):
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.today())
    
    def to_json(self):
        return {
            'id': self.id,
            'title' : self.title,
            'createdAt': self.createdAt
        }
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id = id).first()
    