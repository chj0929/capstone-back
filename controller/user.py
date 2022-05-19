from flask import Blueprint, jsonify

from model.userVO import User
from model.likeslogVO import Likeslog
from utils.auth import login_required

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/')
@login_required
def get_user_list():
  all_user = User.query.all()
  all_user = list(map(lambda x: x.email, all_user))
  return jsonify(all_user)


@bp.get('/<String:user_id>/info')
@login_required
def get_user_info(user_id):
  user_info = User.query.filter_by(id=user_id).all()
  return jsonify(user_info)


@bp.get('/<String:user_id>/likeslog')
@login_required
def get_user_likeslog(user_id):
  likeslog = Likeslog.query.filter_by(u_id=user_id).all()
  likeslog = list(map(lambda x: x.serialize(), likeslog))
  return jsonify(likeslog)
