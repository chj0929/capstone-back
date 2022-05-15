from flask import Flask

from . import main_views, auth, user_views



def create_endpoints(app: Flask):
  app.register_blueprint(main_views.bp)
  app.register_blueprint(auth.bp)
  app.register_blueprint(user_views.bp)

#참조
# https://wikidocs.net/81057

#새로 만든 블루프린트를 사용하려면 pybo/__init__.py 파일에 등록해야한다.
#[파일명: progects/myproject/pybo/__init__.py]
#(... 생략 ...)

#def create_app():
#    (... 생략 ...)

    # 블루프린트
  # from .views import main_views, question_views, answer_views, auth_views
  # app.register_blueprint(main_views.bp)
  # app.register_blueprint(question_views.bp)
  # app.register_blueprint(answer_views.bp)
  # app.register_blueprint(auth_views.bp)
  #
  # (... 생략 ...)

# return app
