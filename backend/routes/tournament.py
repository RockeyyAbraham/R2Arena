"""
Defines API endpoints related to tournaments.
Handles tournament registration and bracket management.
Should remain lightweight with logic handled in services.
Part of the routing layer of the backend.
"""

from flask import Blueprint, jsonify, request
from models.tournament import (
    get_all_tournaments,
    get_tournament_by_id,
    create_tournament,
    delete_tournament
)

# Create the tournament blueprint
tournament_bp = Blueprint('tournament', __name__, url_prefix='/api/tournaments')

@tournament_bp.route('', methods=['GET'])
def get_tournaments():
    """
    GET /api/tournaments
    Retrieves all tournaments from the models layer.
    """
    tournaments = get_all_tournaments()
    return jsonify([t.to_dict() for t in tournaments]), 200

@tournament_bp.route('/<id>', methods=['GET'])
def get_tournament(id):
    """
    GET /api/tournaments/<id>
    Retrieves a single tournament by its unique ID.
    Returns 404 if the tournament is not found.
    """
    tournament = get_tournament_by_id(id)
    if not tournament:
        return jsonify({"error": f"Tournament with ID '{id}' not found."}), 404
    return jsonify(tournament.to_dict()), 200

@tournament_bp.route('', methods=['POST'])
def create_new_tournament():
    """
    POST /api/tournaments
    Creates a new tournament after validating the payload.
    Returns 201 Created on success, or 400 Bad Request on validation error.
    """
    if not request.is_json:
        return jsonify({"error": "Request body must be JSON."}), 400

    data = request.get_json()
    try:
        new_tournament = create_tournament(data)
        return jsonify(new_tournament.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@tournament_bp.route('/<id>', methods=['DELETE'])
def delete_existing_tournament(id):
    """
    DELETE /api/tournaments/<id>
    Deletes an existing tournament by its unique ID.
    Returns 200 on success, or 404 if the tournament is not found.
    """
    success = delete_tournament(id)
    if not success:
        return jsonify({"error": f"Tournament with ID '{id}' not found."}), 404
    return jsonify({"message": f"Tournament with ID '{id}' successfully deleted."}), 200
