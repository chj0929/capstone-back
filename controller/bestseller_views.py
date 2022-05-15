from flask import Blueprint, jsonify

from models.bestseller import Bestseller

bp = Blueprint('Bestseller', __name__, url_prefix='/bestseller')


@bp.route('/')
def get_my_info():
  return 'Best Seller'

@bp.get('/<int:ranking>')
def get_Bestseller_Ranking(ranking):
  print(ranking)
  return 'get_Bestseller_Ranking'

