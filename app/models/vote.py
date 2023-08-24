from app.app import db
from datetime import datetime

class Vote(db.Model):
    __tablename__ = 'votes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id'))
    election_id = db.Column(db.Integer, db.ForeignKey('elections.id'))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
