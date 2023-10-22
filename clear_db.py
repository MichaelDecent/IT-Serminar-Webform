from app.models import User
from app import db, app

app.app_context().push()
users = User.query.all()
for u in users:
    print (u)
    db.session.delete(u)
    db.session.commit()
