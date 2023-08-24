from flask import Blueprint, jsonify, render_template, request

from app.models.vote import Vote

vote_bp = Blueprint('vote', __name__)

@vote_bp.route('/votes', methods=['GET'])
def get_votes():
    votes = Vote.query.all()
    votes_data = [{'id': vote.id, 'user_id': vote.user_id, 'candidate_id': vote.candidate_id} for vote in votes]

    if request.headers.get('Content-Type') == 'application/json':
        return jsonify(votes_data)
    else:
        return render_template('vote/votes.html', votes=votes)
