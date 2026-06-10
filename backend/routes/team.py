"""
Defines API endpoints related to team operations.
Handles requests for team rosters and registration.
Should remain lightweight with logic handled in services.
Part of the routing layer of the backend.
"""

from flask import Blueprint, jsonify
from models.team import get_all_teams

# Create the team blueprint
team_bp = Blueprint('team', __name__, url_prefix='/api/teams')

@team_bp.route('', methods=['GET'])
def get_teams():
    """
    GET /api/teams
    Retrieves all registered esports teams.
    """
    teams = get_all_teams()
    return jsonify([t.to_dict() for t in teams]), 200
