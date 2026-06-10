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

def get_tournament_by_id(tournament_id):
    """
    Finds a tournament by its unique ID.
    Returns the Tournament instance, or None if not found.
    """
    for t in MOCK_TOURNAMENTS:
        if str(t.id) == str(tournament_id):
            return t
    return None

def create_tournament(data):
    """
    Validates data and creates a new tournament in memory.
    Raises ValueError on validation failure.
    """
    # 1. Validation: Name must be non-empty string
    name = data.get("name")
    if not name or not isinstance(name, str) or not name.strip():
        raise ValueError("Tournament name must be a non-empty string.")

    # 2. Validation: Max teams must be a positive integer
    max_teams = data.get("max_teams")
    if max_teams is not None:
        try:
            max_teams = int(max_teams)
            if max_teams <= 0:
                raise ValueError()
        except (ValueError, TypeError):
            raise ValueError("Tournament max_teams must be a positive integer.")
    else:
        max_teams = 32  # Default limit

    # 3. Status must be a string (defaults to 'open' if not provided)
    status = data.get("status", "open")
    if not isinstance(status, str) or not status.strip():
        raise ValueError("Tournament status must be a string.")

    # Optional metadata fields (with default values for R2Arena schema compatibility)
    game = data.get("game", "Unknown Game")
    region = data.get("region", "All India")
    start_date = data.get("start_date", "2026-07-01")
    prize_pool = data.get("prize_pool", "₹0")
    registered_teams = data.get("registered_teams", 0)

    # 4. Generate unique ID
    existing_numeric_ids = []
    for t in MOCK_TOURNAMENTS:
        id_str = str(t.id)
        if id_str.startswith("trn_"):
            try:
                existing_numeric_ids.append(int(id_str.split("_")[1]))
            except (ValueError, IndexError):
                pass
        elif id_str.isdigit():
            existing_numeric_ids.append(int(id_str))

    next_num = max(existing_numeric_ids) + 1 if existing_numeric_ids else 1
    new_id = f"trn_{next_num:03d}"

    # 5. Instantiate and store
    new_tournament = Tournament(
        tournament_id=new_id,
        name=name,
        game=game,
        region=region,
        status=status,
        start_date=start_date,
        prize_pool=prize_pool,
        registered_teams=registered_teams,
        max_teams=max_teams
    )
    MOCK_TOURNAMENTS.append(new_tournament)
    return new_tournament

def delete_tournament(tournament_id):
    """
    Deletes a tournament from memory.
    Returns True if successfully deleted, False if not found.
    """
    global MOCK_TOURNAMENTS
    for i, t in enumerate(MOCK_TOURNAMENTS):
        if str(t.id) == str(tournament_id):
            MOCK_TOURNAMENTS.pop(i)
            return True
    return False

