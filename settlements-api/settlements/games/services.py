from settlements.services import CrudServices, AppServices
from settlements.games.models import Campaign, Player
from settlements.games.schemas import CampaignCreate, CampaignUpdate, PlayerCreate, PlayerUpdate


class CampaignCrud(CrudServices[Campaign, CampaignCreate, CampaignUpdate]):
    pass


class CampaignServices(AppServices[CampaignCrud, Campaign, CampaignCreate, CampaignUpdate]):
    pass


class PlayerCrud(CrudServices[Player, PlayerCreate, PlayerUpdate]):
    pass


class PlayerServices(AppServices[PlayerCrud, Player, PlayerCreate, PlayerUpdate]):
    pass


campaign_services = CampaignServices(CampaignCrud, Campaign)
player_services = PlayerServices(PlayerCrud, Player)
