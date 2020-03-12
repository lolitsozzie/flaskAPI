from basicapi.extensions import db
from .base_model import BaseModel

class user(BaseModel):
    first_name = db.Coulumn(db.Sring)
    email = db.column(db.String)