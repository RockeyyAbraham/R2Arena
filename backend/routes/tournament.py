"""
Defines API endpoints related to tournaments.
Handles tournament registration and bracket management.
Should remain lightweight with logic handled in services.
Part of the routing layer of the backend.
"""

from flask import Blueprint, jsonify

# Create the tournament blueprint
tournament_bp = Blueprint('tournament', __name__, url_prefix='/api/tournaments')

@tournament_bp.route('', methods=['GET'])
def get_tournaments():
    """
    GET /api/tournaments
    Retrieves a list of tournaments including their names, games, status, and prizes.
    """
    sample_tournaments = [
        {
            "id": "trn_001",
            "name": "Varanasi Grassroots BGMI Clash",
            "game": "BGMI",
            "region": "Uttar Pradesh",
            "status": "Upcoming",
            "start_date": "2026-07-01",
            "prize_pool": "₹50,000",
            "registered_teams": 24,
            "max_teams": 32
        },
        {
            "id": "trn_002",
            "name": "Bhopal Valorant Showdown",
            "game": "Valorant",
            "region": "Madhya Pradesh",
            "status": "Ongoing",
            "start_date": "2026-06-15",
            "prize_pool": "₹75,000",
            "registered_teams": 16,
            "max_teams": 16
        },
        {
            "id": "trn_003",
            "name": "Patna Free Fire Frontier",
            "game": "Free Fire",
            "region": "Bihar",
            "status": "Completed",
            "start_date": "2026-05-10",
            "prize_pool": "₹30,000",
            "registered_teams": 32,
            "max_teams": 32
        }
    ]
    return jsonify(sample_tournaments), 200
