from app import db

class Bestseller(db.Model):
  __tablename__= 'bestseller'

  ranking = db.Column(db.Integer, primary_key=True, default=0, nullable=False)
  isbn = db.Column(db.Integer, db.ForeignKey('book.isbn'), default=0, nullable=False)

  @property
  def serialize(self):
    return {
      "ranking": self.ranking,
      "isbn": self.isbn
    }