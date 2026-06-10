"""
Defines the data structure for User entities.
Represents how user data is stored and accessed.
Used by services or routes for database interaction.
Part of the models layer of the backend.
"""

class User:
    """
    User class representing players or admins.
    """
    def __init__(self, user_id, name, username, email, role, region, stats=None):
        self.id = user_id
        self.name = name
        self.username = username
        self.email = email
        self.role = role
        self.region = region
        self.stats = stats or {}

    def to_dict(self):
        """
        Converts the user object into a dictionary for JSON serialization.
        """
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "role": self.role,
            "region": self.region,
            "stats": self.stats
        }

# Mock database table representation
MOCK_USERS = [
    User(
        user_id="usr_98234",
        name="Rockey",
        username="Rockey",
        email="rockey@example.com",
        role="player",
        region="Kerala",
        stats={"matches_played": 12, "wins": 8, "win_rate": 0.67, "rank": "Silver"}
    ),
    User(
        user_id="pl_101",
        name="Player One",
        username="Player1",
        email="player1@example.com",
        role="player",
        region="Uttar Pradesh",
        stats={"matches_played": 45, "wins": 32, "win_rate": 0.71, "rank": "Gold"}
    ),
    User(
        user_id="pl_102",
        name="Player Two",
        username="Player2",
        email="player2@example.com",
        role="player",
        region="Gujarat",
        stats={"matches_played": 60, "wins": 48, "win_rate": 0.80, "rank": "Platinum"}
    )
]

def get_all_players():
    """
    Simulates querying the database for all users with the role 'player'.
    """
    return [u for u in MOCK_USERS if u.role == "player"]

def get_user_by_id(user_id):
    """
    Simulates querying the database for a single user by their unique ID.
    """
    for u in MOCK_USERS:
        if u.id == user_id:
            return u
    return None
