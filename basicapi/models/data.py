import datetime

from ..extensions import db
from .base_model import BaseModel


class Data(BaseModel):
    value = db.Column(db.Float, nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'value': self.value,
            'time': self.created_at
        }