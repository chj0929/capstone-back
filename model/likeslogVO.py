from app import db

class Likeslog(db.Model):
  __tablename__= 'likeslog'

#  U_ID = db.Column(db.Varchar, default=0, primary_key=True, db.ForeignKey('users.id'))
  isbn = db.Column(db.Integer, db.ForeignKey('book.isbn'), nullable=False)
