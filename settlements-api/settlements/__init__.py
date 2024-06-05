import traceback

try:
    from settlements.users.models import User  # noqa: F401
    from settlements.games.models import Campaign, Player  # noqa: F401
    from settlements.cities.models import Settlement, Resource, Construction, ConstructionInfo  # noqa: F401
except ImportError:
    traceback.print_exc()
