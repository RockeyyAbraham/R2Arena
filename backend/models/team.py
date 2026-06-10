"""
Defines the data structure for Team entities.
Represents how team data is stored and accessed.
Used by services or routes for database interaction.
Part of the models layer of the backend.
"""

class Team:
    """
    Team class representing competitive rosters.
    """
    def __init__(self, team_id, name, captain_id, region, members=None):
        self.id = team_id
        self.name = name
        self.captain_id = captain_id
        self.region = region
        self.members = members or []

    def to_dict(self):
        """
        Converts the team object into a dictionary for JSON serialization.
        """
        return {
            "id": self.id,
            "name": self.name,
            "captain_id": self.captain_id,
            "region": self.region,
            "members": self.members
        }

# Mock database table representation
MOCK_TEAMS = [
    Team(
        team_id="tm_201",
        name="Team Rockey",
        captain_id="usr_98234",
        region="Kerala",
        members=["usr_98234"]
    ),
    Team(
        team_id="tm_202",
        name="Alpha Squad",
        captain_id="pl_101",
        region="Uttar Pradesh",
        members=["pl_101", "pl_102"]
    )
]

def get_all_teams():
    """
    Simulates querying the database for all teams.
    """
    return MOCK_TEAMS
