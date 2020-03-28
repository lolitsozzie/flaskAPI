from ..extensions import db
from .base_model import BaseModel


class User(BaseModel):
    first_name = db.Column(db.Text, nullable=False)
    tasks = db.relationship('Task', backref=db.backref('User'))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'tasks': [x.serialize for x in self.tasks]
        }