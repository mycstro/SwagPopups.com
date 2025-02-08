import datetime
import os
from app import db
from sqlalchemy.sql import func

class Message(db.Model):

    __tablename__ =  "message"

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    text = db.Column(db.Text())
    date = db.Column(db.DateTime,default=func.now(),nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    sender = db.relationship("User", foreign_keys=[sender_id])
    recipient = db.relationship("User", foreign_keys=[recipient_id])
    
    def __init__(self, text, sender_id, recipient_id):
        self.text = text
        self.sender_id = sender_id
        self.recipient_id = recipient_id
        