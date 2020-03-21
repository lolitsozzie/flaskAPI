import datetime

from ..extensions import db
from .base_model import BaseModel


class Data(BaseModel):
    value = db.Column(db.Integer, nullable=False)

    @classmethod
    def get_all(cls):
        """
        Get all product variations for a practice
        :return: (list) of ProductVariation objects
        """
        return [c for c in cls.query.all()]
    @property
    def serialize(self):
        return {
            'id': self.id,
            'value': self.value,
            'time': self.created_at
        }