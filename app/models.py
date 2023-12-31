from app import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    userprename = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pp = db.Column(db.String(255),nullable=True)

    def __repr__(self):
        return f"User('{self.username}','{self.userprename}', '{self.email}','{self.pp})"
    
    @classmethod
    def get_all_users(cls):
        return cls.query.all()

class UserPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    userprename = db.Column(db.String(100), nullable=False)
    ucontent = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    pp = db.Column (db.String(255),nullable=True)

    def __repr__(self):
        return f"UserPost('{self.uid}',{self.username}','{self.userprename}','{self.ucontent}', '{self.email},'{self.pp}')"
    
    @classmethod
    def get_all_post(cls):
        return cls.query.all()

# Heroku pass: Thinolord2k3@