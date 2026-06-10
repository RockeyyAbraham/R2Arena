"""
Defines API endpoints related to player operations.
Handles requests for player profiles and stats.
Should remain lightweight with logic handled in services.
Part of the routing layer of the backend.
"""

from flask import Blueprint, jsonify
from models.user import get_all_players

# Create the player blueprint
player_bp = Blueprint('player', __name__, url_prefix='/api/players')

@player_bp.route('', methods=['GET'])
def get_players():
    """
    GET /api/players
    Retrieves a list of registered grassroots players with their statistics from the models layer.
    """
    players = get_all_players()
    formatted_players = [{
        "id": p.id,
        "name": p.name,
        "gamer_tag": p.username,
        "region": p.region,
        "stats": p.stats
    } for p in players]
    return jsonify(formatted_players), 200
