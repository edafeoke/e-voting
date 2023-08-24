from flask import Blueprint, jsonify, render_template, request

from app.models.user import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_data = [{'id': user.id, 'username': user.username, 'role': user.role} for user in users]

    if request.headers.get('Content-Type') == 'application/json':
        return jsonify(users_data)
    else:
        return render_template('user/users.html', users=users)
        # return jsonify(users_data)