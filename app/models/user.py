from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    user_name = db.Column(db.String(200))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)

    def __str__(self):
        return self.public_id
