from flask import Blueprint, jsonify

from models.bestseller import Bestseller

bp = Blueprint('Book', __name__, url_prefix='/book_detail')


@bp.route('/')
def get_my_info():
  return 'Book'

@bp.get('/<int:isbn>')
def get_Book(isbn):
  print(isbn)
  return 'get_Book'

@bp.get('/<String:title>')
def get_Name(title):
  print(title)
  return 'get_title'

@bp.get('/<String:author>')
def get_Author(author):
  print(author)
  return 'get_author'

@bp.get('/<String:publisher>')
def get_Publisher(publisher):
  print(publisher)
  return 'get_Publisher'

@bp.get('/<String:Genre>')
def get_Genre(genre):
  print(genre)
  return 'get_Genre'

@bp.get('/<String:Info>')
def get_Info(info):
  print(info)
  return 'get_Info'

@bp.get('/<Float:Average>')
def get_Average(average):
  print(average)
  return 'get_Average'

@bp.get('/<int:Count>')
def get_Count(count):
  print(count)
  return 'get_Count'

@bp.get('/<int:Listprice>')
def get_Listprice(listprice):
  print(listprice)
  return 'get_Listprice'

@bp.get('/<int:Price>')
def get_Price(price):
  print(price)
  return 'get_Price'

@bp.get('/<int:Page>')
def get_Page(page):
  print(page)
  return 'get_Page'

@bp.get('/<int:Likes>')
def get_Likes(likes):
  print(likes)
  return 'get_Likes'

@bp.get('/<Varchar:Img_url>')
def get_Img(img_url):
  return 'get_Img_url'
