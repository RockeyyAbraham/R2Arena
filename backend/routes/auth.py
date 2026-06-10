"""
Defines API endpoints related to authentication.
Handles login, registration, and session management.
Should remain lightweight with logic handled in services.
Part of the routing layer of the backend.
"""

from flask import Blueprint, jsonify

# Create the authentication blueprint
auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/status', methods=['GET'])
def get_auth_status():
    """
    GET /api/auth/status
    Retrieves the current authentication status and mock logged-in user profile.
    """
    return jsonify({
        "authenticated": True,
        "user": {
            "id": "usr_98234",
            "username": "raju_gamer",
            "email": "raju.abraham@example.in",
            "role": "player",
            "region": "Madhya Pradesh",
            "joined_at": "2026-01-15T10:00:00Z"
        }
    }), 200
