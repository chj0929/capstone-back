from flask import Flask

from . import auth, user, bestseller, book_detail



def create_endpoints(app: Flask):
  app.register_blueprint(auth.bp)
  app.register_blueprint(user.bp)
  app.register_blueprint(bestseller.bp)
  app.register_blueprint(book_detail.bp)

  return app
