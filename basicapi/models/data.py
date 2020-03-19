from ..extensions import db
from .base_model import BaseModel


class Data(BaseModel):
    value = db.Column(db.Text, nullable=False)

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
            'value': self.value,
            'id': self.id
        }