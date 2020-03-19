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

    @classmethod
    def get(cls, object_id):
        """
        Get an object by id.

        :param object_id: object's id
        :return: Object
        """
        try:
            queried_object = cls.query.filter_by(id=int(object_id)).one_or_none()
            if queried_object and hasattr(queried_object, 'current_user_authorized'):
                return queried_object if queried_object.current_user_authorized else None
            return queried_object
        except:
            return None