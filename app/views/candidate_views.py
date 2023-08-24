from flask import Blueprint, jsonify, render_template, request

from app.models.candidate import Candidate

candidate_bp = Blueprint('candidate', __name__)

@candidate_bp.route('/candidates', methods=['GET'])
def get_candidates():
    candidates = Candidate.query.all()
    candidates_data = [{'id': candidate.id, 'name': candidate.name, 'election_id': candidate.election_id} for candidate in candidates]

    if request.headers.get('Content-Type') == 'application/json':
        return jsonify(candidates_data)
    else:
        return render_template('candidate/candidates.html', candidates=candidates)
