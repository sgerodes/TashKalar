from enum import Enum


class Rank(Enum):
    COMMON = 0
    HEROIC = 1
    LEGENDARY = 2


class Faction(Enum):
    SYLVAN = 0
    HIGHLAND = 1
    SOUTHERN = 2
    NORTHERN = 3
    EVERFROST = 4
    NETHERVOID = 5
    ETHERWEAVE = 6


class Type(Enum):
    FLARE = 0
    LEGEND = 1
    CREATURE = 2


class Point:
    def __init__(self, x, y, piece):
        self.x = x
        self.y = y
        self.piece = piece


class Pattern:
    pass


class Card:
    def __init__(self, name: str, rank: Rank, faction: Faction, summon_pattern, effect_text=""):
        self.name = name
        self.faction = faction
        self.rank = rank
        self.summon_pattern = summon_pattern
        self.summon_cost_common = 0  # number of common pieces needed to summon this beeing
        self.summon_cost_heroic = 0  # number of heroic pieces needed to summon this beeing
        self.summon_cost_total = self.summon_cost_common + self.summon_cost_heroic
        self.effect_text = effect_text

