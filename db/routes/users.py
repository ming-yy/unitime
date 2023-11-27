from flask import Blueprint, jsonfiy
from app.daos import user_dao

user_bp = Blueprint('user_bp', __name__)

@user_bp.route("/api/users", methods=["GET"])
def get_users():
    return jsonify(user_dao.get_all())

@user_bp.route("/api/users/<int:user_id>", methods=["POST"])
def update_user(user_id):
    data = request.json    
    user = user_service.update_user(user_id, data)
    return jsonify(user)