from app import db

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  email = db.Column(db.String(30), unique=True)
  password = db.Column(db.String(100))
  nickname = db.Column(db.String(30))
  user_class = db.Column(db.String(10))

  @property
  def serialize(self):
    return {
      "id": self.id,
      "email": self.email,
      "password": self.password,
      "nickname": self.nickname,
      "user_class": self.user_class
    }

