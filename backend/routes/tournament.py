"""
Defines API endpoints related to tournaments.
Handles tournament registration and bracket management.
Should remain lightweight with logic handled in services.
Part of the routing layer of the backend.
"""

from flask import Blueprint, jsonify
from models.tournament import get_all_tournaments

# Create the tournament blueprint
tournament_bp = Blueprint('tournament', __name__, url_prefix='/api/tournaments')

@tournament_bp.route('', methods=['GET'])
def get_tournaments():
    """
    GET /api/tournaments
    Retrieves a list of tournaments including their names, games, status, and prizes from the models layer.
    """
    tournaments = get_all_tournaments()
    return jsonify([t.to_dict() for t in tournaments]), 200
