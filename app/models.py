from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), index=True)
    lastname = db.Column(db.String(64), index=True)
    address = db.Column(db.String(64), index=True)
    email = db.Column(db.String(64), index=True, unique=True)
    age = db.Column(db.Integer, index=True)
    itIntention = db.Column(db.Integer, index=True)
    expectation = db.Column(db.String(256), index=True)

    def __repr__(self):
        return f"<User's First Name => {self.firstname} and Last Name => {self.lastname}>"