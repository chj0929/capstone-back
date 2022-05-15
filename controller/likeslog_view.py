from flask import Blueprint, jsonify

from models.likeslog import Likeslog

bp = Blueprint('Likeslog', __name__, url_prefix='/likeslog')


@bp.route('/')
def get_my_info():
  return 'Likeslog'

@bp.get('/<int:isbn>')
def get_Likeslog(isbn):
  print(isbn)
  return 'get_Likeslog'