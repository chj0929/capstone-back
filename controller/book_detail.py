from flask import Blueprint, request, jsonify, Response, session

from app import db
from utils.auth import login_required
from model.bookVO import Book
from model.likeslogVO import Likeslog
from model.reviewVO import Review

bp = Blueprint('Book', __name__, url_prefix='/book_detail')

@bp.get('/<int:isbn>')
@login_required
def get_book(isbn):
  book_isbn = isbn

  if book_isbn:
    book = Book.query.filter(Book.isbn == book_isbn).first()
    if book != None:
      return book
    else:
      return Response(status=404)
  else:
    return '잘못된 도서 코드입니다.'

@bp.post('/')
@login_required
def register_new_book():
  new_book_file = request.files['file']
  db.session.add(new_book_file)
  db.session.commit()

def get_book_reviews(isbn):
  book_isbn = isbn

  if book_isbn:
    reviews = Book.query.filter_by(Review.isbn == book_isbn).all()
    if reviews != None:
      return jsonify(reviews)
    else:
      return Response(status=404)
  else:
    return Response(status=404)


def toggle_user_likeslog(): # 도서 찜 등록 /찜 취소
  req = request.json
  isbn = req.get('isbn')
  user_id = session.get('userid')

  # 이전에 찜한 적 있는지 확인
  likeslog = Likeslog.query.filter_by(isbn=isbn, u_id=user_id).first()

  if likeslog is not None: # 예전에 찜한 도서라면
    db.session.delete(likeslog) # db에서 삭제
    db.session.commit()
    return '찜목록 제외 성공', 200

  else: # 예전에 찜한 도서가 아니라면
    new_likeslog = Likeslog(isbn=isbn, u_id=user_id)
    db.session.add(new_likeslog)
    db.session.commit()
    return '찜목록 추가 성공', 200