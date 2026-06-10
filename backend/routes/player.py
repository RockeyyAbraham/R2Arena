"""
Defines API endpoints related to player operations.
Handles requests for player profiles and stats.
Should remain lightweight with logic handled in services.
Part of the routing layer of the backend.
"""

from flask import Blueprint, jsonify

# Create the player blueprint
player_bp = Blueprint('player', __name__, url_prefix='/api/players')

@player_bp.route('', methods=['GET'])
def get_players():
    """
    GET /api/players
    Retrieves a list of registered grassroots players with their statistics.
    """
    sample_players = [
        {
            "id": "pl_101",
            "name": "Rohan Sharma",
            "gamer_tag": "RohanViper",
            "region": "Uttar Pradesh",
            "stats": {
                "matches_played": 45,
                "wins": 32,
                "win_rate": 0.71,
                "rank": "Gold"
            }
        },
        {
            "id": "pl_102",
            "name": "Ananya Patel",
            "gamer_tag": "PhoenixIn",
            "region": "Gujarat",
            "stats": {
                "matches_played": 60,
                "wins": 48,
                "win_rate": 0.80,
                "rank": "Platinum"
            }
        },
        {
            "id": "pl_103",
            "name": "Kabir Singh",
            "gamer_tag": "KabirOnyx",
            "region": "Punjab",
            "stats": {
                "matches_played": 30,
                "wins": 15,
                "win_rate": 0.50,
                "rank": "Silver"
            }
        }
    ]
    return jsonify(sample_players), 200
