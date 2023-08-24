from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from app.models.election import Election
from app.models.candidate import Candidate
from app.models.vote import Vote
from app.app import db

vote_bp = Blueprint('vote', __name__)

@vote_bp.route('/<int:election_id>/vote/<int:candidate_id>', methods=['POST'])
@login_required
def vote(election_id, candidate_id):
    election = Election.query.get_or_404(election_id)
    candidate = Candidate.query.get_or_404(candidate_id)

    existing_vote = Vote.query.filter_by(user_id=current_user.id, election_id=election_id).first()
    if existing_vote:
        flash('You have already voted in this election.', 'warning')
        return redirect(url_for('election.list_elections'))

    new_vote = Vote(user_id=current_user.id, election_id=election_id, candidate_id=candidate_id)
    db.session.add(new_vote)
    db.session.commit()

    flash('Vote submitted successfully!', 'success')
    return redirect(url_for('election.list_elections'))
