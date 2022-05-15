from app import db

class Book(db.Model):
  __tablename__= 'book'

  isbn = db.Column(db.Integer, default=0, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  author = db.Column(db.String(50), nullable=False)
  publisher = db.Column(db.String(50), nullable=False)
  genre = db.Column(db.String(50), nullable=False)
  info = db.Column(db.String(500), nullable=False)
  average = db.Column(db.Float, nullable=False)
  count = db.Column(db.Integer, default=0, nullable=False)
  listprice = db.Column(db.Integer, default=0, nullable=False)
  price = db.Column(db.Integer, default=0, nullable=False)
  page = db.Column(db.Integer, default=0, nullable=False)
  likes = db.Column(db.Integer, default=0, nullable=True)
  img_url = db.Column(db.String(500), nullable=False)

  @property
  def serialize(self):
    return {
      "isbn": self.isbn,
      "title": self.title,
      "author": self.author,
      "publisher": self.publisher,
      "genre": self.genre,
      "info": self.info,
      "average": self.average,
      "count": self.count,
      "listprice": self.listprice,
      "price": self.price,
      "page": self.page,
      "likes": self.likes,
      "img_url": self.img_url
    }