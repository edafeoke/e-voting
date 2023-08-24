from flask import Blueprint, jsonify, render_template, request

from app.models.election import Election
from app.models.candidate import Candidate

election_bp = Blueprint('election', __name__)

@election_bp.route('/elections', methods=['GET'])
def get_elections():
    elections = Election.query.all()
    elections_data = [{'id': election.id, 'title': election.title} for election in elections]

    if request.headers.get('Content-Type') == 'application/json':
        return jsonify(elections_data)
    else:
        return render_template('election/elections.html', elections=elections)

@election_bp.route('/elections/<int:election_id>/candidates', methods=['GET'])
def get_candidates(election_id):
    candidates = Candidate.query.filter_by(election_id=election_id).all()
    candidates_data = [{'id': candidate.id, 'name': candidate.name} for candidate in candidates]

    if request.headers.get('Content-Type') == 'application/json':
        return jsonify(candidates_data)
    else:
        return render_template('election/candidates.html', candidates=candidates)
