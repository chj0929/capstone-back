from app import db

class Review(db.Model):
  __tablename__= 'review'

  r_id = db.Column(db.Integer, default=0, primary_key=True, autoincrement=True)
  u_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  isbn = db.Column(db.Integer, db.ForeignKey('book.isbn'), nullable=False)
  rating = db.Column(db.Float, nullable=False)
  reviewtxt = db.Column(db.String(50), nullable=False)

  @property
  def serialize(self):
    return {
      "r_id": self.r_id,
      "u_id": self.u_id,
      "isbn": self.isbn,
      "rating": self.rating,
      "reviewtxt": self.reviewtxt
    }