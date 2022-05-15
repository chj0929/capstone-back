from flask import Blueprint, jsonify

from models.review import Review

bp = Blueprint('Review', __name__, url_prefix='/review')


@bp.route('/')
def get_my_info():
  return 'Review'

@bp.get('/<Varchar:REVIEWTXT>')
def get_Review(REVIEWTXT):
  print(REVIEWTXT)
  return 'get_Review'