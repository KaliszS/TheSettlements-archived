module default {

    scalar type BuildingType extending enum<
        Townhall,
        Barracks,
        Wall
    >;

    scalar type UnitType extending enum<
        Swordsman,
        Archer,
        Spearman,
        Cavalry,
        Catapult
    >;


    type Building {
        required name: BuildingType;
        required effect: str;
        required levels: array<
            tuple<level: int16, effect: str, cost: int16>
        >;
    };

    type Unit {
        required name: UnitType;
        required cost: int16;
        required attack: int16;
        required defense: int16;
        required speed: int16;
        required capacity: int16;
    };

    type GameSession {
        required map_size: tuple<x: int16, y: int16>;
    };

    type User {
        required username: str;
        required password: str;
        required hashed_password: str;
        required email: str;
        required is_superuser: bool;
        multi active_game_sessions: GameSession;

    };

    type Settlement {
        required name: str;
        required owner: User;
        required location: tuple<x: int16, y: int16>;
        required populations: int16;
        multi buildings: Building;
        multi units: Unit;
    };

};
