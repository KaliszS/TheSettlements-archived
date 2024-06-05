CREATE MIGRATION m1trixoyvwsdzccw3gnvsmondaiikkc2tehaqrftiddadsp37srugq
    ONTO initial
{
  CREATE SCALAR TYPE default::BuildingType EXTENDING enum<Townhall, Barracks, Wall>;
  CREATE TYPE default::Building {
      CREATE REQUIRED PROPERTY levels: array<tuple<level: std::int16, effect: std::str, cost: std::int16>>;
      CREATE REQUIRED PROPERTY effect: std::str;
      CREATE REQUIRED PROPERTY name: default::BuildingType;
  };
  CREATE SCALAR TYPE default::UnitType EXTENDING enum<Swordsman, Archer, Spearman, Cavalry, Catapult>;
  CREATE TYPE default::Unit {
      CREATE REQUIRED PROPERTY attack: std::int16;
      CREATE REQUIRED PROPERTY capacity: std::int16;
      CREATE REQUIRED PROPERTY cost: std::int16;
      CREATE REQUIRED PROPERTY defense: std::int16;
      CREATE REQUIRED PROPERTY name: default::UnitType;
      CREATE REQUIRED PROPERTY speed: std::int16;
  };
  CREATE TYPE default::GameSession {
      CREATE REQUIRED PROPERTY map_size: tuple<x: std::int16, y: std::int16>;
  };
  CREATE TYPE default::User {
      CREATE MULTI LINK active_game_sessions: default::GameSession;
      CREATE REQUIRED PROPERTY email: std::str;
      CREATE REQUIRED PROPERTY hashed_password: std::str;
      CREATE REQUIRED PROPERTY is_superuser: std::bool;
      CREATE REQUIRED PROPERTY password: std::str;
      CREATE REQUIRED PROPERTY username: std::str;
  };
  CREATE TYPE default::Settlement {
      CREATE MULTI LINK buildings: default::Building;
      CREATE REQUIRED LINK owner: default::User;
      CREATE MULTI LINK units: default::Unit;
      CREATE REQUIRED PROPERTY location: tuple<std::int16, std::int16>;
      CREATE REQUIRED PROPERTY name: std::str;
      CREATE REQUIRED PROPERTY populations: std::int16;
  };
};
