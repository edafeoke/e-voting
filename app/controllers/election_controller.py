from flask import Blueprint, render_template

from app.models.election import Election
from app.models.candidate import Candidate

election_bp = Blueprint('election', __name__)

@election_bp.route('/create')
def create_election():
    return render_template('election/create.html')

@election_bp.route('/list')
def list_elections():
    elections = Election.query.all()
    return render_template('election/list.html', elections=elections)

@election_bp.route('/<int:election_id>/candidates')
def view_candidates(election_id):
    election = Election.query.get_or_404(election_id)
    candidates = Candidate.query.filter_by(election_id=election_id).all()
    return render_template('election/candidates.html', election=election, candidates=candidates)
