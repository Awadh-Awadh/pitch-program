from app import db

class Pitch(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    pitch = db.column(db.String(255))
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)
    def __repr__(self):
        return '<User %r>' % self.pitch



class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    email = db.Column(db.String(255), unique = True, nullable = False)
    
    
    def __repr__(self):
        return '<User %r>' % self.username


