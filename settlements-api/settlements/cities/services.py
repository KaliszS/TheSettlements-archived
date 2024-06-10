from settlements.services import CrudServices, AppServices
from settlements.cities.models import Settlement
from settlements.cities.schemas import SettlementCreate, SettlementUpdate


class SettlementCrud(CrudServices[Settlement, SettlementCreate, SettlementUpdate]):
    pass


class SettlementServices(AppServices[SettlementCrud, Settlement, SettlementCreate, SettlementUpdate]):
    pass


settlement_services = SettlementServices(SettlementCrud, Settlement)
