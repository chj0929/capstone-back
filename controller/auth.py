from flask import Blueprint, request, session
import bcrypt

from app import db
from model.userVO import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.get('/signup')
def signup():
  user_info = request.args
  user_email = request.args.get("email")

  if user_info.get('email') and user_info.get('pw') and user_info.get('nickname'):
    user = User.query.filter(User.email == user_email).first()
    if user != None:
      return '다른이메일 선택해주세요'
    else:
      encrypted = bcrypt.hashpw(user_info.get('pw').encode('utf-8'), bcrypt.gensalt())
      new_user = User(email=user_info.get('email'), password=encrypted, nickname=user_info.get('nickname'))
      db.session.add(new_user)
      db.session.commit()
      return '회원 가입 성공'
  else:
    return '입력 누락!!!'


@bp.get('/login')
def login():

  user_info = request.args
  user_email = request.args.get("email")
  user_pw = request.args.get('pw')

  if user_info.get('email') and user_info.get('pw'):
    user = User.query.filter_by(User.email == user_email).first()
    if bcrypt.checkpw(user_pw.encode('utf-8'), user.password.encode('utf-8')):
      session['userid'] = user.id
      return '로그인 성공'
    else:
      return '비밀번호 틀림'
  else:
    return '로그인 실패', 401


@bp.route('/logout')
def logout():
    session.clear()
    return '로그아웃 성공'