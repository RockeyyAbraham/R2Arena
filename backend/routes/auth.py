"""
Defines API endpoints related to authentication.
Handles login, registration, and session management.
Should remain lightweight with logic handled in services.
Part of the routing layer of the backend.
"""

from flask import Blueprint, jsonify
from models.user import get_user_by_id

# Create the authentication blueprint
auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/status', methods=['GET'])
def get_auth_status():
    """
    GET /api/auth/status
    Retrieves the current authentication status and active user profile from models.
    """
    # Simulates querying database for the currently logged-in user
    user = get_user_by_id("usr_98234")
    if user:
        return jsonify({
            "authenticated": True,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role,
                "region": user.region,
                "joined_at": "2026-01-15T10:00:00Z"
            }
        }), 200
    else:
        return jsonify({
            "authenticated": False,
            "user": None
        }), 401
