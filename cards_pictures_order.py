from models import Faction, NonFactionType


cards_manual_metadata_ordered = {
    NonFactionType.LEGEND.value: [
        {
            "name": "Fire Dragon",
            "common_cost": 1,
            "upgraded_cost": 3,
        },
        {
            "name": "Hell Bull",
            "common_cost": 4,
            "upgraded_cost": 2,
        },
        {
            "name": "Angel of Death",
            "common_cost": 5,
            "upgraded_cost": 1,
        },
        {
            "name": "The Eldest Tree",
            "common_cost": 2,
            "upgraded_cost": 2,
        },
        {
            "name": "Bone Catapult",
            "common_cost": 1,
            "upgraded_cost": 3,
        },
        {
            "name": "Fire  Elemental",
            "common_cost": 3,
            "upgraded_cost": 2,
        },
        {
            "name": "Leviathan",
            "common_cost": 1,
            "upgraded_cost": 3,
        },
        {
            "name": "Two-Headed Dragon",
            "common_cost": 2,
            "upgraded_cost": 3,
        },
        {
            "name": "Earth Elemental",
            "common_cost": 2,
            "upgraded_cost": 3,
        },
        {
            "name": "Time Elemental",
            "common_cost": 2,
            "upgraded_cost": 3,
        },
        {
            "name": "Storm Elemental",
            "common_cost": 1,
            "upgraded_cost": 3,
        },
        {
            "name": "Titan",
            "common_cost": 3,
            "upgraded_cost": 2,
        },
    ]
}



cards_pictures_order = {
    Faction.ETHERWEAVE.value: [
        "Doppelganger",
        "Paradox Worm",
        "Lesser Shadow Twin",
        "Translocationist",
        "Antimatter Spirit",
        "Merchant of Time",
        "Gate of Oblivion",
        "Time Traveler",
        "Greater Shadow Twin",
        "Warpmaster",
        "Dark Sphere",
        "Void Summoner",
        "Eternal Emperor",
        "Reality Patch",
        "Polarity Queen",
        "Singularity",
        "Ziggurat Sentinel",
        "Iris of Eternity",
    ],
    Faction.IMPERIAL.value: [
        "Swordmaster",
        "Messenger",
        "Herald",
        "Bomb",
        "Chronicler",
        "Assassin",
        "Time Mage",
        "Summoner",
        "Hypnotist",
        "Cannon",
        "Champion",
        "Infantry Captain",
        "Cavalry Captain",
        "Gryphon Rider",
        "Knight",
        "High Priestess",
        "Master of Intrigue",
        "Gun Tower"
    ],
}
cards_pictures_order['Northern'] = cards_pictures_order.get('Imperial')
cards_pictures_order['Southern'] = cards_pictures_order.get('Imperial')

cards_pictures_stats = {
    Faction.ETHERWEAVE.value: {
        "Doppelganger": {'cost': 2},
        "Paradox Worm": {'cost': 3},
        "Lesser Shadow Twin": {'cost': 3},
        "Translocationist": {'cost': 4},
        "Antimatter Spirit": {'cost': 2},
        "Merchant of Time": {'cost': 4},
        "Gate of Oblivion": {'cost': 4},
        "Time Traveler": {'cost': 3},
        "Greater Shadow Twin": {'cost': 3},
        "Warpmaster": {'cost': 3},
        "Dark Sphere": {'cost': 4},
        "Void Summoner": {'cost': 4},
        "Eternal Emperor": {'cost': 4},
        "Reality Patch": {'cost': 4},
        "Polarity Queen": {'cost': 4},
        "Singularity": {'cost': 4},
        "Ziggurat Sentinel": {'cost': 5},
        "Iris of Eternity": {'cost': 5},
    },
    Faction.IMPERIAL.value: {
        "Swordmaster": {'cost': 2},
        "Messenger": {'cost': 2},
        "Herald": {'cost': 3},
        "Bomb": {'cost': 2},
        "Chronicler": {'cost': 3},
        "Assassin": {'cost': 3},
        "Time Mage": {'cost': 4},
        "Summoner": {'cost': 3},
        "Hypnotist": {'cost': 4},
        "Cannon": {'cost': 3},
        "Champion": {'cost': 4},
        "Infantry Captain": {'cost': 4},
        "Cavalry Captain": {'cost': 4},
        "Gryphon Rider": {'cost': 4},
        "Knight": {'cost': 4},
        "High Priestess": {'cost': 4},
        "Master of Intrigue": {'cost': 4},
        "Gun Tower": {'cost': 4},
    }
}
cards_pictures_stats['Northern'] = cards_pictures_stats.get('Imperial')
cards_pictures_stats['Southern'] = cards_pictures_stats.get('Imperial')

flare_stats = {
    0: {},
    1: {},
    2: {},
    3: {
        "upgraded": "Place 1 common piece of your color on any empty square.",
        "pieces": "Place 1 common piece of your color on any empty square, or convert 1 common enemy piece to your color.",
        "pieces_cost": 4,
        "upgraded_cost": 5
    },
    4: {
        "upgraded": "Do 1 standard move with one of your common pieces, or upgrade 1 of your common pieces.",
        "pieces": "Place 2 common pieces of your color on empty squares.",
        "pieces_cost": 3,
        "upgraded_cost": 6
    },
    5: {
        "upgraded": "Place 1 common piece of your color on any empty square, or upgrade 1 of your common pieces.",
        "pieces": "You may do 1 combat leap with one of your common pieces.",
        "pieces_cost": 4,
        "upgraded_cost": 4
    },
    6: {
        "upgraded": "Place 1 common piece of your color on any empty square.",
        "pieces": "Upgrade 1 of your common pieces. Gain an action.",
        "pieces_cost": 4,
        "upgraded_cost": 6
    },
    7: {
        "upgraded": "Gain an action.",
        "pieces": "Place 1 common piece of your color on any empty square.",
        "pieces_cost": 4,
        "upgraded_cost": 5
    },
    8: {
        "upgraded": "Place 1 heroic piece of your color on any empty square.",
        "pieces": "You may do 1 standard move and 1 combat move (in either order), using your common pieces.",
        "pieces_cost": 5,
        "upgraded_cost": 4
    },
    9: {},
    10: {
        "upgraded": "Place 1 common piece of your color on any empty square.",
        "pieces": "You may do 1 combat move or 2 standard moves, using your non-legendary pieces.",
        "pieces_cost": 3,
        "upgraded_cost": 4
    },
    11: {
        "upgraded": "You may do up to 3 standard moves, using your common pieces.",
        "pieces": "Gain an action.",
        "pieces_cost": 2,
        "upgraded_cost": 5
    }
}
