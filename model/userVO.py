from app import db

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  email = db.Column(db.String(30), unique=True)
  password = db.Column(db.String(100))
  nickname = db.Column(db.String(30))
  user_class = db.Column(db.String(10))

  # comment = db.relationship('Comment', backref='user')

  def serialize(self):
    return {
      "id": self.id,
      "email": self.email,
      "password": self.password,
      "nickname": self.nickname,
      "user_class": self.user_class
    }

# https://riptutorial.com/flask/example/31786/relationships--one-to-many
# https://opentutorials.org/module/3669/22070
# https://www.youtube.com/watch?v=eip6UTUG60I