"""
Defines the data structure for Tournament entities.
Represents how tournament data is stored and accessed.
Used by services or routes for database interaction.
Part of the models layer of the backend.
"""

class Tournament:
    """
    Tournament class representing competitive events.
    """
    def __init__(self, tournament_id, name, game, region, status, start_date, prize_pool, registered_teams=0, max_teams=32):
        self.id = tournament_id
        self.name = name
        self.game = game
        self.region = region
        self.status = status
        self.start_date = start_date
        self.prize_pool = prize_pool
        self.registered_teams = registered_teams
        self.max_teams = max_teams

    def to_dict(self):
        """
        Converts the tournament object into a dictionary for JSON serialization.
        """
        return {
            "id": self.id,
            "name": self.name,
            "game": self.game,
            "region": self.region,
            "status": self.status,
            "start_date": self.start_date,
            "prize_pool": self.prize_pool,
            "registered_teams": self.registered_teams,
            "max_teams": self.max_teams
        }

# Mock database table representation
MOCK_TOURNAMENTS = [
    Tournament(
        tournament_id="trn_001",
        name="BGMI Championship",
        game="BGMI",
        region="All India",
        status="Upcoming",
        start_date="2026-07-01",
        prize_pool="₹1,00,000",
        registered_teams=10,
        max_teams=64
    ),
    Tournament(
        tournament_id="trn_002",
        name="Valorant Open",
        game="Valorant",
        region="All India",
        status="Ongoing",
        start_date="2026-06-15",
        prize_pool="₹2,00,000",
        registered_teams=16,
        max_teams=16
    )
]

def get_all_tournaments():
    """
    Simulates querying the database for all tournaments.
    """
    return MOCK_TOURNAMENTS
