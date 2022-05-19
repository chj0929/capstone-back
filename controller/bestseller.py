from flask import Blueprint, jsonify, request, session, render_template
from flask_sqlalchemy import SQLAlchemy

from model.bestsellerVO import Bestseller

bp = Blueprint('Book', __name__, url_prefix='/bestseller')
db = SQLAlchemy()

@bp.get('/')
def get_bestseller():
  bestseller = Bestseller.query.order_by(Bestseller.ranking).all()
  return jsonify(bestseller)

@bp.post('/')
def update_bestseller():
  update_file = request.files['file']
  db.session.add(update_file)
  db.session.commit()

@bp.delete('/')
def clear_bestseller():
  Bestseller.query.delete()