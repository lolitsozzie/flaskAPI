from sqlalchemy import func

from basicapi.extensions import db


class BaseModel(db.Model):
    """
    Base model used for all models.
    """
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.statement_timestamp())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.statement_timestamp(),
                           onupdate=func.clock_timestamp())
    