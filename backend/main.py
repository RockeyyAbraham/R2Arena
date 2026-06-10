"""
Main entry point of the Flask application.
Initializes the app and registers routes.
Acts as the central connection between all modules.
Responsible for starting the backend server.
"""

import os
import sys

# Ensure backend directory is in the Python search path to resolve blueprint imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, jsonify
from routes.auth import auth_bp
from routes.player import player_bp
from routes.tournament import tournament_bp
from routes.team import team_bp

# Initialize Flask application
app = Flask(__name__)

# Register all API route blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(player_bp)
app.register_blueprint(tournament_bp)
app.register_blueprint(team_bp)

@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify the service status.
    """
    return jsonify({
        "status": "online",
        "service": "R2 Arena Backend"
    }), 200

if __name__ == '__main__':
    # Start the backend server locally on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
