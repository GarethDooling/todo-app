from application import db
from application.models import Teams

db.drop_all()
db.create_all()