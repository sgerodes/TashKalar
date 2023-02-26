from enum import Enum
import typing as t


class SpecialTextType(Enum):
    WARP_TEXT = 'warptext'
    FROZEN_TEXT = 'frozentext'


class Rank(Enum):
    COMMON = "common"
    HEROIC = "heroic"
    LEGENDARY = "legendary"

    def is_upgraded(self):
        return self is self.HEROIC or self is self.LEGENDARY


class Card:
    image_width = None
    image_height = None

    def __init__(self):
        self.pilImage = None


class FlareCard(Card):
    image_width = 250
    image_height = 420

    def __init__(self):
        super().__init__()
        self.upgraded_text = None
        self.pieces_text = None
        self.upgraded_cost = None
        self.pieces_cost = None


class TaskCard(Card):
    image_width = 406
    image_height = 240

    def __init__(self):
        self.name = None
        self.text = None
        super().__init__()


class CreatureCard(Card):
    image_width = 250
    image_height = 420

    def __init__(self):
        super().__init__()
        self.name = None
        self.text = None
        self.common_cost = None


class LegendaryCard(CreatureCard):
    def __init__(self):
        super().__init__()
        self.rank: str = Rank.LEGENDARY.value
        self.upgraded_cost = None

    def get_total_cost(self) -> int:
        return self.common_cost + self.upgraded_cost


class FactionCreatureCard(CreatureCard):
    def __init__(self):
        super().__init__()
        self.rank: str = None
        self.faction: str = None
        self.special_text = None
        self.special_text_type: t.Optional[SpecialTextType] = None


class Faction(Enum):
    SYLVAN = "Sylvan"
    SOUTHERN = "Southern"
    NORTHERN = "Northern"
    IMPERIAL = "Imperial"
    HIGHLAND = "Highland"
    EVERFROST = "Everfrost"
    NETHERVOID = "Nethervoid"
    ETHERWEAVE = "Etherweave"

    def is_imperial(self):
        return self is self.NORTHERN or self is self.SOUTHERN

class NonFactionType(Enum):
    LEGEND = "Legends"
    FLARE = "Flare"
    TASK = "task"