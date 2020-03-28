from ..extensions import db
from .base_model import BaseModel


class Task(BaseModel):
    description = db.Column(db.Text, nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'description': self.description,
            'start': self.start,
            'end': self.end
        }