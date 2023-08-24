from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

migrate = Migrate(app, db)
login_manager = LoginManager(app)
CORS(app)  # Enable CORS for API routes

# Create the database tables within an application context
with app.app_context():
    from app.models.user import User
    from app.models.vote import Vote
    from app.models.election import Election
    from app.models.candidate import Candidate
    db.create_all()



# Register blueprints
from app.controllers import user_controller, election_controller, vote_controller, candidate_controller

# app.register_blueprint(user_controller.user_bp, name='user')
# app.register_blueprint(election_controller.election_bp, name='election')
# app.register_blueprint(vote_controller.vote_bp, name='vote')
# app.register_blueprint(candidate_controller.candidate_bp, name='candidate')

# Import and register views for JSON APIs
from app.views import user_views, election_views, vote_views, candidate_views

app.register_blueprint(user_views.user_bp, url_prefix='/api')
app.register_blueprint(election_views.election_bp, url_prefix='/api')
app.register_blueprint(vote_views.vote_bp, url_prefix='/api')
app.register_blueprint(candidate_views.candidate_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
