from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required

from app.models.candidate import Candidate
from app.app import db

candidate_bp = Blueprint('candidate', __name__)

@candidate_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_candidate():
    if request.method == 'POST':
        name = request.form.get('name')
        election_id = request.form.get('election_id')

        new_candidate = Candidate(name=name, election_id=election_id)
        db.session.add(new_candidate)
        db.session.commit()

        flash('Candidate added successfully!', 'success')
        return redirect(url_for('election.list_elections'))

    # Render a form to create a new candidate
    return render_template('candidate/create.html')
