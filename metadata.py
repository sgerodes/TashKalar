from models import Faction, NonFactionType

all_manual_metadata_ordered = {
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
            "name": "Fire Elemental",
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
            "common_cost": 3,
            "upgraded_cost": 2,
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
    ],
    Faction.ETHERWEAVE.value: [
        {'name': 'Doppelganger', 'common_cost': 2},
        {'name': 'Paradox Worm', 'common_cost': 3},
        {'name': 'Lesser Shadow Twin', 'common_cost': 3},
        {'name': 'Translocationist', 'common_cost': 4},
        {'name': 'Antimatter Spirit', 'common_cost': 2},
        {'name': 'Merchant of Time', 'common_cost': 4},
        {'name': 'Gate of Oblivion', 'common_cost': 4},
        {'name': 'Time Traveler', 'common_cost': 3},
        {'name': 'Greater Shadow Twin', 'common_cost': 3},
        {'name': 'Warpmaster', 'common_cost': 3},
        {'name': 'Dark Sphere', 'common_cost': 4},
        {'name': 'Void Summoner', 'common_cost': 4},
        {'name': 'Eternal Emperor', 'common_cost': 4},
        {'name': 'Reality Patch', 'common_cost': 4},
        {'name': 'Polarity Queen', 'common_cost': 4},
        {'name': 'Singularity', 'common_cost': 4},
        {'name': 'Ziggurat Sentinel', 'common_cost': 5},
        {'name': 'Iris of Eternity', 'common_cost': 5},
    ],
    Faction.IMPERIAL.value: [
        {'name': 'Swordmaster', 'common_cost': 2},
        {'name': 'Messenger', 'common_cost': 2},
        {'name': 'Herald', 'common_cost': 3},
        {'name': 'Bomb', 'common_cost': 2},
        {'name': 'Chronicler', 'common_cost': 3},
        {'name': 'Assassin', 'common_cost': 3},
        {'name': 'Time Mage', 'common_cost': 4},
        {'name': 'Summoner', 'common_cost': 3},
        {'name': 'Hypnotist', 'common_cost': 4},
        {'name': 'Cannon', 'common_cost': 3},
        {'name': 'Champion', 'common_cost': 4},
        {'name': 'Infantry Captain', 'common_cost': 4},
        {'name': 'Cavalry Captain', 'common_cost': 4},
        {'name': 'Gryphon Rider', 'common_cost': 4},
        {'name': 'Knight', 'common_cost': 4},
        {'name': 'High Priestess', 'common_cost': 3},
        {'name': 'Master of Intrigue', 'common_cost': 4},
        {'name': 'Gun Tower', 'common_cost': 4},
    ],
    Faction.SYLVAN.value: [
        {'name': 'Sapling', 'common_cost': 2},
        {'name': 'Kiskin Farseeders', 'common_cost': 2},
        {'name': 'Charging Buck', 'common_cost': 3},
        {'name': 'Forest Wardens', 'common_cost': 2},
        {'name': 'Naiad', 'common_cost': 3},
        {'name': 'Kiskin Spirit', 'common_cost': 3},
        {'name': 'Dryad', 'common_cost': 3},
        {'name': 'Centaur Spearman', 'common_cost': 4},
        {'name': 'Centaur Chieftain', 'common_cost': 4},
        {'name': 'Unicorn', 'common_cost': 4},
        {'name': 'Sylvan Queen', 'common_cost': 4},
        {'name': 'Sylvan Princess', 'common_cost': 3},
        {'name': 'Woodland Druid', 'common_cost': 3},
        {'name': 'Forest Ancient', 'common_cost': 4},
        {'name': 'Forest Mystic', 'common_cost': 3},
        {'name': 'Kiskin Leafsplitter', 'common_cost': 4},
        {'name': 'Kiskin Boughrunner', 'common_cost': 4},
        {'name': 'Tree Shepherd', 'common_cost': 4},
    ],
    Faction.HIGHLAND.value: [
        {'name': 'Wild Eagle', 'common_cost': 2},
        {'name': 'Clan Axeman', 'common_cost': 2},
        {'name': 'Clan Healer', 'common_cost': 3},
        {'name': 'Dire Wolf', 'common_cost': 3},
        {'name': 'Ritual Keeper', 'common_cost': 2},
        {'name': 'Eagle Lord', 'common_cost': 4},
        {'name': 'Wolf Rider', 'common_cost': 4},
        {'name': 'Blood Shaman', 'common_cost': 4},
        {'name': 'War Drummer', 'common_cost': 4},
        {'name': 'Hill Giant', 'common_cost': 4},
        {'name': 'Warlord', 'common_cost': 5},
        {'name': 'War Summoner', 'common_cost': 4},
        {'name': 'Ritual Master', 'common_cost': 3},
        {'name': 'Legend Slayer', 'common_cost': 4},
        {'name': 'Mountain Troll', 'common_cost': 4},
        {'name': 'Hungry Bear', 'common_cost': 3},
        {'name': 'Werewolf', 'common_cost': 3},
        {'name': 'Clan Guardian', 'common_cost': 3},
    ],
    Faction.EVERFROST.value: [
        {'name': 'Snow Fox', 'common_cost': 2},
        {'name': 'Royal Reindeer', 'common_cost': 3},
        {'name': 'Crystal Mirror', 'common_cost': 2},
        {'name': 'Crystal Grower', 'common_cost': 2},
        {'name': 'Ice Princess', 'common_cost': 3},
        {'name': 'Ice Queen', 'common_cost': 4},
        {'name': 'Frostweave Summoner', 'common_cost': 3},
        {'name': 'Winter Whisperer', 'common_cost': 4},
        {'name': 'Frozen Chest', 'common_cost': 3},
        {'name': 'Everfrost Sentinel', 'common_cost': 4},
        {'name': 'Glacier Giant', 'common_cost': 4},
        {'name': 'Polar Bear', 'common_cost': 4},
        {'name': 'War Sled', 'common_cost': 4},
        {'name': 'Snow Monster', 'common_cost': 4},
        {'name': 'Frost Imp', 'common_cost': 3},
        {'name': 'Ice Wyvern', 'common_cost': 4},
        {'name': 'Deathbringer', 'common_cost': 4},
        {'name': 'Frostweave Illusionist', 'common_cost': 3},
    ],
    Faction.NETHERVOID.value: [
        {'name': 'Shadow Imp', 'common_cost': 2},
        {'name': 'Flame Imp', 'common_cost': 2},
        {'name': 'Gate Keeper', 'common_cost': 3},
        {'name': 'Demon of Gluttony', 'common_cost': 3},
        {'name': 'Demon of Pride', 'common_cost': 3},
        {'name': 'Acolyte of Destruction', 'common_cost': 3},
        {'name': 'Acolyte of Growth', 'common_cost': 4},
        {'name': 'Power Seeker', 'common_cost': 4},
        {'name': 'Hell Hound', 'common_cost': 4},
        {'name': 'Vortex Master', 'common_cost': 4},
        {'name': 'Gate Master', 'common_cost': 5},
        {'name': 'Hell Rider', 'common_cost': 4},
        {'name': 'Demon of Wrath', 'common_cost': 4},
        {'name': 'Demon of Greed', 'common_cost': 4},
        {'name': 'Demon of Lust', 'common_cost': 4},
        {'name': 'Demon of Sloth', 'common_cost': 1},
        {'name': 'Demon of Envy', 'common_cost': 3},
        {'name': 'Possessed Summoner', 'common_cost': 4},
    ],
    NonFactionType.TASK.value: [
        # Destruction tasks
        {'name': 'Destruction', 'points': 1},
        {'name': 'Devastation', 'points': 2},
        {'name': 'Heroic Destruction', 'points': 2},
        {'name': 'Heroic Devastation', 'points': 3},
        {'name': 'End of Legends', 'points': 2},

        # Color control
        {'name': 'Red Conquest', 'points': 2},
        {'name': 'Green Conquest', 'points': 2},
        {'name': 'Color Conquest', 'points': 3},
        {'name': 'Red Legends', 'points': 3},
        {'name': 'Green Legends', 'points': 3},
        {'name': 'Rainbow Dominance', 'points': 2},

        ## Sumoning
        # Color Summoning
        {'name': 'Red Summoning', 'points': 1},
        {'name': 'Green Summoning', 'points': 1},
        {'name': 'Colored Summoning', 'points': 2},
        # Other Summoning
        {'name': 'Legendary Summoning', 'points': 2},

        # Area Dominance
        {'name': 'Central Dominance', 'points': 1},
        {'name': 'Center Cross', 'points': 2},
        {'name': 'Line Dominance', 'points': 2},
        {'name': 'Diagonals', 'points': 3},

        # Chains
        {'name': 'Corner Chain', 'points': 3},
        {'name': 'Side Chain', 'points': 3},

        # Piece control
        {'name': 'Imprisonment', 'points': 1},
        {'name': 'Envelopment', 'points': 2},
        {'name': 'Isolation', 'points': 2},
    ],
    NonFactionType.FLARE.value: [
        {
            'name': 0,
            "type": "Flare",
            "upgraded": "Place 1 common piece of your color on any empty square.",
            "pieces": "Place 1 heroic piece of your color on any empty square.",
            "pieces_cost": 6,
            "upgraded_cost": 3
        },
        {
            'name': 1,
            "type": "Flare",
            "upgraded": "Place 1 common piece of your color on any empty square.",
            "pieces": "Place 1 common piece of your color on any empty square.",
            "pieces_cost": 4,
            "upgraded_cost": 4
        },
        {
            'name': 2,
            "type": "Flare",
            "upgraded": "You may do up to 3 standard moves, using your common pieces.",
            "pieces": "Gain an action.",
            "pieces_cost": 5,
            "upgraded_cost": 3
        },
        {
            'name': 3,
            "upgraded": "Place 1 common piece of your color on any empty square.",
            "pieces": "Place 1 common piece of your color on any empty square, or convert 1 common enemy piece to your color.",
            "pieces_cost": 5,
            "upgraded_cost": 4
        },
        {
            'name': 4,
            "upgraded": "Do 1 standard move with one of your common pieces, or upgrade 1 of your common pieces.",
            "pieces": "Place 2 common pieces of your color on empty squares.",
            "pieces_cost": 6,
            "upgraded_cost": 3
        },
        {
            'name': 5,
            "upgraded": "Place 1 common piece of your color on any empty square, or upgrade 1 of your common pieces.",
            "pieces": "You may do 1 combat leap with one of your common pieces.",
            "pieces_cost": 4,
            "upgraded_cost": 4
        },
        {
            'name': 6,
            "upgraded": "Place 1 common piece of your color on any empty square.",
            "pieces": "Upgrade 1 of your common pieces. Gain an action.",
            "pieces_cost": 6,
            "upgraded_cost": 4
        },
        {
            'name': 7,
            "upgraded": "Gain an action.",
            "pieces": "Place 1 common piece of your color on any empty square.",
            "pieces_cost": 5,
            "upgraded_cost": 4
        },
        {
            'name': 8,
            "upgraded": "Place 1 heroic piece of your color on any empty square.",
            "pieces": "You may do 1 standard move and 1 combat move (in either order), using your common pieces.",
            "pieces_cost": 4,
            "upgraded_cost": 5
        },
        {
            'name': 9,
            "type": "Flare",
            "upgraded": "Place 2 common pieces of your color on empty squares.",
            "pieces": "Place 1 common piece of your color on any empty square.",
            "pieces_cost": 5,
            "upgraded_cost": 5
        },
        {
            'name': 10,
            "upgraded": "Place 1 common piece of your color on any empty square.",
            "pieces": "You may do 1 combat move or 2 standard moves, using your non-legendary pieces.",
            "pieces_cost": 4,
            "upgraded_cost": 3
        },
        {
            'name': 11,
            "upgraded": "You may do up to 3 standard moves, using your common pieces.",
            "pieces": "Gain an action.",
            "pieces_cost": 5,
            "upgraded_cost": 2
        }
    ]
}


all_manual_metadata_ordered[Faction.SOUTHERN.value] = all_manual_metadata_ordered.get(Faction.IMPERIAL.value)
all_manual_metadata_ordered[Faction.NORTHERN.value] = all_manual_metadata_ordered.get(Faction.IMPERIAL.value)

all_fetched_metadata = {
    "Sylvan": {
        "Tree Shepherd": {
            "type": "Sylvan",
            "name": "Tree Shepherd",
            "text": "Choose 1 of your pieces: If it is common, upgrade it; if heroic, it may do 1 combat move; if legendary, it may do 1 standard move."
        },
        "Kiskin Boughrunner": {
            "type": "Sylvan",
            "name": "Kiskin Boughrunner",
            "text": "The Kiskin Boughrunner may do up to 3 combat moves. Each move must end on a square adjacent to one of your pieces."
        },
        "Naiad": {
            "type": "Sylvan",
            "name": "Naiad",
            "text": "You may choose up to 2 of your pieces adjacent to the Naiad and do 1 standard move with each."
        },
        "Charging Buck": {
            "type": "Sylvan",
            "name": "Charging Buck",
            "text": "The Charging Buck may do up to 2 combat leaps, each of distance exactly 2."
        },
        "Woodland Druid": {
            "type": "Sylvan",
            "name": "Woodland Druid",
            "text": "Upgrade 1 common piece of each color."
        },
        "Forest Ancient": {
            "type": "Sylvan",
            "name": "Forest Ancient",
            "text": "Place 2 enemy common pieces on empty squares up to distance 2. Then destroy 2 common pieces of the same color or colors up to distance 3."
        },
        "Kiskin Spirit": {
            "type": "Sylvan",
            "name": "Kiskin Spirit",
            "text": "You may choose a card from your discard pile and put it on top of your deck. If you do, or if your discard pile was empty, draw 1 extra card from your deck at the end of this turn."
        },
        "Sapling": {
            "type": "Sylvan",
            "name": "Sapling",
            "text": "Upgrade the Sapling after summoning it."
        },
        "Centaur Chieftain": {
            "type": "Sylvan",
            "name": "Centaur Chieftain",
            "text": "The Centaur Chieftain may do 1 combat move. If he does, you may do up to 3 combat moves in the same direction, using other pieces of yours."
        },
        "Sylvan Queen": {
            "type": "Sylvan",
            "name": "Sylvan Queen",
            "text": "You may convert 1 non-legendary enemy piece on a diagonally adjacent square to your piece of the same rank."
        },
        "Forest Mystic": {
            "type": "Sylvan",
            "name": "Forest Mystic",
            "text": "At the end of this turn, draw 1 extra card from your deck and 1 extra card from the legendary deck."
        },
        "Unicorn": {
            "type": "Sylvan",
            "name": "Unicorn",
            "text": "Choose one: Either the Unicorn may do 1 combat move, or you gain 1 action."
        },
        "Centaur Spearman": {
            "type": "Sylvan",
            "name": "Centaur Spearman",
            "text": "The Centaur Spearman may do 1 combat move. If he does, destroy the next piece in the same direction, unless it is legendary."
        },
        "Forest Wardens": {
            "type": "Sylvan",
            "name": "Forest Wardens",
            "text": "Destroy 1 common piece of an opponent with more common pieces than you. Destroy 1 heroic piece of an opponent with more upgraded pieces than you."
        },
        "Sylvan Princess": {
            "type": "Sylvan",
            "name": "Sylvan Princess",
            "text": "You may convert 1 common enemy piece on a diagonally adjacent square to your common piece."
        },
        "Kiskin Leafsplitter": {
            "type": "Sylvan",
            "name": "Kiskin Leafsplitter",
            "text": "Up to 2 times, you may choose a diagonal direction and destroy the first piece in that direction."
        },
        "Dryad": {
            "type": "Sylvan",
            "name": "Dryad",
            "text": "On one of the adjacent squares, you may convert 1 non-legendary enemy piece to your common piece."
        },
        "Kiskin Farseeders": {
            "type": "Sylvan",
            "name": "Kiskin Farseeders",
            "text": "You may place 1 common piece of your color on an empty square adjacent to one of your pieces."
        }
    },
    "Imperial": {
        "Infantry Captain": {
            "type": "Imperial",
            "name": "Infantry Captain",
            "text": "Do up to 2 combat moves, using your pieces other than the Infantry Captain."
        },
        "Chronicler": {
            "type": "Imperial",
            "name": "Chronicler",
            "text": "Upgrade 1 of your common pieces other than the Chronicler. Then that piece may do a standard move."
        },
        "Gun Tower": {
            "type": "Imperial",
            "name": "Gun Tower",
            "text": "You may choose 1 of the indicated directions: Destroy the first 2 pieces in that direction. A legendary piece cannot be destroyed and stops the shot."
        },
        "Knight": {
            "type": "Imperial",
            "name": "Knight",
            "text": "The Knight may do up to 3 combat moves. You cannot destroy common pieces with these moves."
        },
        "Cannon": {
            "type": "Imperial",
            "name": "Cannon",
            "text": "You may choose 1 of the indicated directions: Destroy all common pieces in that direction."
        },
        "Messenger": {
            "type": "Imperial",
            "name": "Messenger",
            "text": "You may choose 1 of your non-legendary pieces and a direction. That piece may do any number of standard moves in that direction."
        },
        "Herald": {
            "type": "Imperial",
            "name": "Herald",
            "text": "Do up to 2 moves, using only your pieces. These moves can only be onto empty squares."
        },
        "Champion": {
            "type": "Imperial",
            "name": "Champion",
            "text": "You may destroy 1 adjacent enemy piece. If that piece was legendary, you also destroy the Champion and gain an action."
        },
        "Summoner": {
            "type": "Imperial",
            "name": "Summoner",
            "text": "You may place up to 2 common pieces of your color on empty marked squares."
        },
        "Cavalry Captain": {
            "type": "Imperial",
            "name": "Cavalry Captain",
            "text": "You may choose 1 of your pieces other than the Cavalry Captain: You may do up to 1 combat move and up to 2 standard moves with it (in any order)."
        },
        "Bomb": {
            "type": "Imperial",
            "name": "Bomb",
            "text": "If summoning the Bomb is your last action this turn, nothing happens ; otherwise, destroy the Bomb and all common pieces adjacent to it."
        },
        "Master of Intrigue": {
            "type": "Imperial",
            "name": "Master of Intrigue",
            "text": "Do up to 3 moves: standard moves with the Master of Intrigue and/or combat moves using non-legendary pieces that were used to summon him."
        },
        "High Priestess": {
            "type": "Imperial",
            "name": "High Priestess",
            "text": "The High Priestess may do 1 standard move. Whether she moves or not, you may then upgrade 1 common piece adjacent to her."
        },
        "Hypnotist": {
            "type": "Imperial",
            "name": "Hypnotist",
            "text": "You may choose up to 3 common or up to 2 heroic pieces in one enemy color: Do 1 combat move with each."
        },
        "Gryphon Rider": {
            "type": "Imperial",
            "name": "Gryphon Rider",
            "text": "The Gryphon Rider may do a combat leap. If she does, you may then downgrade her and place 1 common piece of your color on an empty adjacent space."
        },
        "Assassin": {
            "type": "Imperial",
            "name": "Assassin",
            "text": "Destroy any piece on the marked square. If the marked square was empty, the Assassin may move onto it."
        },
        "Time Mage": {
            "type": "Imperial",
            "name": "Time Mage",
            "text": "Gain an action. If there is an enemy piece on the marked square, destroy it."
        },
        "Swordmaster": {
            "type": "Imperial",
            "name": "Swordmaster",
            "text": "You may destroy 1 common enemy piece on a diagonally adjacent square. If you do, upgrade the Swordmaster."
        }
    },
    "Highland": {
        "Mountain Troll": {
            "type": "Highland",
            "name": "Mountain Troll",
            "text": "Destroy all common enemy pieces on adjacent squares. If you destroy at least 2 this way, gain an action."
        },
        "Hungry Bear": {
            "type": "Highland",
            "name": "Hungry Bear",
            "text": "The hungry bear may do up to 2 standard moves. If it moves onto an empty square, it stops moving."
        },
        "Hill Giant": {
            "type": "Highland",
            "name": "Hill Giant",
            "text": "Destroy all non-legendary pieces on orthogonally adjacent squares."
        },
        "Ritual Master": {
            "type": "Highland",
            "name": "Ritual Master",
            "text": "If the Ritual Master was summoned on a green square, gain 2 actions; if on a red square, you may destroy 1 heroic and/or 1 common piece anywhere on the board."
        },
        "Clan Healer": {
            "type": "Highland",
            "name": "Clan Healer",
            "text": "You may place up to 2 common pieces of your color. Each must be placed on an empty square adjacent to a green square."
        },
        "Eagle Lord": {
            "type": "Highland",
            "name": "Eagle Lord",
            "text": "The Eagle Lord may do a combat leap to any square of the board."
        },
        "Clan Guardian": {
            "type": "Highland",
            "name": "Clan Guardian",
            "text": "You may upgrade 1 common piece used to summon the Clan Guardian."
        },
        "Blood Shaman": {
            "type": "Highland",
            "name": "Blood Shaman",
            "text": "Destroy 1 non-legendary piece. If it was on a red square, destroy all common pieces adjacent to the red square."
        },
        "Wild Eagle": {
            "type": "Highland",
            "name": "Wild Eagle",
            "text": "The Wild Eagle may do a combat leap to any square of the board."
        },
        "Ritual Keeper": {
            "type": "Highland",
            "name": "Ritual Keeper",
            "text": "If the Ritual Keeper was summoned on a green square, upgrade one of your common pieces; if on a red square, you may do 1 combat move with 1 of your pieces."
        },
        "Dire Wolf": {
            "type": "Highland",
            "name": "Dire Wolf",
            "text": "The Dire Wolf may do up to 2 combat moves."
        },
        "War Summoner": {
            "type": "Highland",
            "name": "War Summoner",
            "text": "Gain an action. For the pattern of the next being you summon this turn, you may use one enemy piece as though it were yours."
        },
        "War Drummer": {
            "type": "Highland",
            "name": "War Drummer",
            "text": "Do either 1 combat move or up to 2 standard moves, using your pieces other than the War Drummer."
        },
        "Warlord": {
            "type": "Highland",
            "name": "Warlord",
            "text": "Do up to 3 combat moves, using your pieces. If you do all 3, at least one has to be with the Warlord."
        },
        "Wolf Rider": {
            "type": "Highland",
            "name": "Wolf Rider",
            "text": "The Wolf Rider may do up to 2 combat moves."
        },
        "Werewolf": {
            "type": "Highland",
            "name": "Werewolf",
            "text": "If the Werewolf was summoned on a non-central red or green square, it may do up to 3 combat moves. Otherwise it may do 1 standard move."
        },
        "Clan Axeman": {
            "type": "Highland",
            "name": "Clan Axeman",
            "text": "You may destroy 1 non-legendary piece on an orthogonally adjacent square."
        },
        "Legend Slayer": {
            "type": "Highland",
            "name": "Legend Slayer",
            "text": "You may destroy 1 legendary or up to 2 non-legendary pieces on diagonally adjacent squares."
        }
    },
    "Everfrost": {
        "Snow Monster": {
            "type": "Everfrost",
            "name": "Snow Monster",
            "text": "Destroy each common enemy piece that is within distance 2 of the Snow Monster and adjacent to at least one of your pieces."
        },
        "Polar Bear": {
            "type": "Everfrost",
            "name": "Polar Bear",
            "text": "The Polar Bear may do a combat move. If that move destroys a piece, it may do a standard move. If that destroys a piece, it may do a move onto an empty square."
        },
        "Winter Whisperer": {
            "type": "Everfrost",
            "name": "Winter Whisperer",
            "text": "",
            "frozentext": "You may destroy one of your common pieces. You may discard 1 flare. If you do both, gain an action."
        },
        "Ice Wyvern": {
            "type": "Everfrost",
            "name": "Ice Wyvern",
            "text": "The Ice Wyvern may do a combat leap to anywhere on the board. If the leap destroys a piece, destroy the Ice Wyvern.",
            "frozentext": "Place a common piece of your color on an empty square adjacent to one of your heroic pieces."
        },
        "Deathbringer": {
            "type": "Everfrost",
            "name": "Deathbringer",
            "text": "You may destroy an adjacent piece; if heroic, it must be adjacent to at least 1 other piece of yours; if legendary, 3 other pieces of yours. Count it as two destroyed pieces. Remove it from the game."
        },
        "Frost Imp": {
            "type": "Everfrost",
            "name": "Frost Imp",
            "text": "You may choose an adjacent common piece and a direction: That piece does as many standard moves as it can in that direction."
        },
        "Ice Princess": {
            "type": "Everfrost",
            "name": "Ice Princess",
            "text": "You may do 1 combat move with one of your common pieces other than the Ice Princess.",
            "frozentext": "Do 1 standard move with one of your common pieces."
        },
        "Everfrost Sentinel": {
            "type": "Everfrost",
            "name": "Everfrost Sentinel",
            "text": "If summoning the Everfrost Sentinel destroyed an enemy piece, you may downgrade the Everfrost Sentinel. If you do, each other player or team has 1 less action on their next turn."
        },
        "Glacier Giant": {
            "type": "Everfrost",
            "name": "Glacier Giant",
            "text": "The Glacier Giant may do any number of combat moves in one of the indicated directions. If it moves, it may continue 1 more square to destroy a legendary piece, but this also destroys the Glacier Giant."
        },
        "Frostweave Illusionist": {
            "type": "Everfrost",
            "name": "Frostweave Illusionist",
            "text": "Convert the Frostweave Illusionist to a common piece of an enemy color.",
            "frozentext": "Convert any common enemy piece to your common piece."
        },
        "War Sled": {
            "type": "Everfrost",
            "name": "War Sled",
            "text": "The War Sled may do up to 3 combat moves, the first in one of the indicated directions and each subsequent move in a direction that differs by no more than 45 degrees from the previous move."
        },
        "Ice Queen": {
            "type": "Everfrost",
            "name": "Ice Queen",
            "text": "You may do 1 combat move with one of your heroic pieces other than the Ice Queen.",
            "frozentext": "Do 1 standard move with one of your heroic pieces."
        },
        "Frostweave Summoner": {
            "type": "Everfrost",
            "name": "Frostweave Summoner",
            "text": "",
            "frozentext": "Use just before summoning a being. For the pattern of that being, you may use one enemy piece as though it were yours."
        },
        "Snow Fox": {
            "type": "Everfrost",
            "name": "Snow Fox",
            "text": "The Snow Fox may do up to 2 standard moves."
        },
        "Crystal Mirror": {
            "type": "Everfrost",
            "name": "Crystal Mirror",
            "text": "You may choose 1 heroic or up to 2 common pieces on yellow-marked squares: For each, place one of your pieces with the same rank on the mirror-image square, if it is empty."
        },
        "Royal Reindeer": {
            "type": "Everfrost",
            "name": "Royal Reindeer",
            "text": "The Royal Reindeer may do a combat leap to a distance of exactly 2. If neither the summoning nor the leap destroys a piece, upgrade the Royal Reindeer."
        },
        "Frozen Chest": {
            "type": "Everfrost",
            "name": "Frozen Chest",
            "text": "You may take one frozen effect from your discard pile and put it directly into play. (The limit of 1 frozen effect in play still applies.)"
        },
        "Crystal Grower": {
            "type": "Everfrost",
            "name": "Crystal Grower",
            "text": "Upgrade 1 common piece of each enemy color.",
            "frozentext": "Upgrade a common piece of your color."
        }
    },
    "Nethervoid": {
        "Demon of Lust": {
            "type": "Nethervoid",
            "name": "Demon of Lust",
            "text": "Choose up to 2 pieces (not necessarily yours). With each, do 1 combat move toward the Gateway. These moves must not destroy the Gateway."
        },
        "Acolyte of Growth": {
            "type": "Nethervoid",
            "name": "Acolyte of Growth",
            "text": "Place a common piece of your color on an empty square. If the Gateway is on a green square, place a heroic piece of your color on an empty square adjacent to that new common piece."
        },
        "Vortex Master": {
            "type": "Nethervoid",
            "name": "Vortex Master",
            "text": "You may do 1 combat move with the Gateway. Whether you do or not, you may then do 1 combat move with one of your pieces adjacent to the Gateway."
        },
        "Demon of Gluttony": {
            "type": "Nethervoid",
            "name": "Demon of Gluttony",
            "text": "The Demon of Gluttony may do a combat move. If this destroys a piece, upgrade Gluttony and it may do another combat move.  If this destroys another piece, Gluttony becomes the Gateway."
        },
        "Demon of Sloth": {
            "type": "Nethervoid",
            "name": "Demon of Sloth",
            "text": "Spend an action to do nothing. If you cannot, destroy the Gateway instead."
        },
        "Acolyte of Destruction": {
            "type": "Nethervoid",
            "name": "Acolyte of Destruction",
            "text": "Destroy a common piece. If the Gateway is on a red square, you may also destroy a heroic piece adjacent to the destroyed piece's square."
        },
        "Possessed Summoner": {
            "type": "Nethervoid",
            "name": "Possessed Summoner",
            "text": "Place a common enemy piece on an empty square adjacent to a piece of the same color. For your next summoning this turn, use pieces of that color instead of your own. You may discard your flare to gain an action."
        },
        "Shadow Imp": {
            "type": "Nethervoid",
            "name": "Shadow Imp",
            "text": "The Shadow Imp may do 1 combat move. If it does and it is not the Gateway, then the Gateway may do 1 combat move in the same direction"
        },
        "Gate Keeper": {
            "type": "Nethervoid",
            "name": "Gate Keeper",
            "text": "You may upgrade any one of your common pieces or place a common piece of your color on an empty square.  In either case, that piece becomes the Gateway."
        },
        "Demon of Envy": {
            "type": "Nethervoid",
            "name": "Demon of Envy",
            "text": "Place a common piece of your color on an empty square adjacent to the Gateway. Then repeat this until there is no such empty square or until no opponent has more pieces than you do."
        },
        "Demon of Greed": {
            "type": "Nethervoid",
            "name": "Demon of Greed",
            "text": "Destroy one of your common and one of your heroic non-Gateway pieces. For each destroyed piece, gain an action."
        },
        "Flame Imp": {
            "type": "Nethervoid",
            "name": "Flame Imp",
            "text": "You may destroy a common piece adjacent to the Gateway."
        },
        "Power Seeker": {
            "type": "Nethervoid",
            "name": "Power Seeker",
            "text": "If the Power Seeker is the Gateway, it may do 1 standard move. Otherwise, it may do any number of combat moves towards the Gateway."
        },
        "Gate Master": {
            "type": "Nethervoid",
            "name": "Gate Master",
            "text": "Upgrade the Gateway. Then choose 1 of your non-legendary pieces to become the Gateway. If upgrading created a legendary piece, then Gate Master's summoning counts as summoning a legend on Gate Master's square."
        },
        "Hell Rider": {
            "type": "Nethervoid",
            "name": "Hell Rider",
            "text": "If the Hell Rider is the Gateway, it may do 1 combat move. Otherwise, it may do up to 3 combat moves."
        },
        "Demon of Wrath": {
            "type": "Nethervoid",
            "name": "Demon of Wrath",
            "text": "Destroy all enemy common pieces adjacent to the Gateway. If there are none, the Gateway may do a standard move first."
        },
        "Demon of Pride": {
            "type": "Nethervoid",
            "name": "Demon of Pride",
            "text": "Upgrade the Demon of Pride. It becomes the Gateway. It may do 1 combat move."
        },
        "Hell Hound": {
            "type": "Nethervoid",
            "name": "Hell Hound",
            "text": "You may destroy an adjacent piece. If you destroy no legendary piece and if your deck is not out of cards, put this card on the bottom of your deck."
        }
    },
    "Etherweave": {
        "Greater Shadow Twin": {
            "type": "Etherweave",
            "name": "Greater Shadow Twin",
            "text": "If Lesser Shadow Twin is in your discard pile, you may destroy one heroic piece adjacent to at least two of your pieces.",
            "warptext": "Upgrade 1 of your common pieces."
        },
        "Iris of Eternity": {
            "type": "Etherweave",
            "name": "Iris of Eternity",
            "text": "You may either destroy an adjacent legendary piece or upgrade the Iris. If the Iris becomes legendary, count it as a legend summoned this turn and discard all your legendary cards."
        },
        "Antimatter Spirit": {
            "type": "Etherweave",
            "name": "Antimatter Spirit",
            "text": "",
            "warptext": "Place a common piece of your color on an empty colorless square. It does a combat move. Place a common piece of another color on the same empty square. It does a combat move in the opposite direction. This is a linked effect."
        },
        "Dark Sphere": {
            "type": "Etherweave",
            "name": "Dark Sphere",
            "text": "Choose up to 3 non-legendary pieces, at most 2 of one color. With each, do a combat move. Each move must end at distance 2 from the Dark Sphere."
        },
        "Polarity Queen": {
            "type": "Etherweave",
            "name": "Polarity Queen",
            "text": "Choose 2 of your non-legendary pieces other than the Queen. Do 1 combat move with each of them in opposite directions. This is a linked effect.",
            "warptext": "Place a common piece of your color on an empty square adjacent to an enemy piece."
        },
        "Doppelganger": {
            "type": "Etherweave",
            "name": "Doppelganger",
            "text": "If you have a pending being, copy its warp effect."
        },
        "Reality Patch": {
            "type": "Etherweave",
            "name": "Reality Patch",
            "text": "In each enemy color, you may destroy 1 heroic piece. You may discard your pending being. You may discard one card of any type from your hand."
        },
        "Paradox Worm": {
            "type": "Etherweave",
            "name": "Paradox Worm",
            "text": "You may swap one of your non-legendary pieces with an enemy piece of the same rank.",
            "warptext": "Upgrade 1 enemy common piece. You may then discard your pending being."
        },
        "Ziggurat Sentinel": {
            "type": "Etherweave",
            "name": "Ziggurat Sentinel",
            "text": "You may either copy a warp effect on a card in your discard pile, or do up to 3 combat moves with Ziggurat Sentinel in the marked direction.",
            "warptext": "Do 1 combat move or 2 standard moves with one of your non-legendary pieces."
        },
        "Merchant of Time": {
            "type": "Etherweave",
            "name": "Merchant of Time",
            "text": "If there is a piece on this card, do a standard leap with that piece to any colorless square on the board.",
            "warptext": "Take a piece from a colorless square and put it on this card. This card cannot be copied. If pending, it cannot be discarded or returned to hand."
        },
        "Time Traveler": {
            "type": "Etherweave",
            "name": "Time Traveler",
            "text": "Time Traveler's summoning square can be any colorless empty square. You may destroy an adjacent common piece. If you do, put the top card of your discard pile on top of your deck."
        },
        "Singularity": {
            "type": "Etherweave",
            "name": "Singularity",
            "text": "Choose an empty colorless square. All common pieces adjacent to that square must do a combat move onto it in the order of your choosing."
        },
        "Gate of Oblivion": {
            "type": "Etherweave",
            "name": "Gate of Oblivion",
            "text": "Destroy any piece on the purple marked square. On another marked square, you may destroy a non-legendary piece.",
            "warptext": "For the rest of this turn, when you destroy a piece count it as though you also destroyed an additional piece of the same color and rank."
        },
        "Void Summoner": {
            "type": "Etherweave",
            "name": "Void Summoner",
            "text": "For your next summoning this turn, you may count up to two empty squares as common pieces of your color.",
            "warptext": "Do a standard move with one of your non-legendary pieces."
        },
        "Eternal Emperor": {
            "type": "Etherweave",
            "name": "Eternal Emperor",
            "text": "If you have not played Eternal Emperor's warp effect this turn, you may perform it now as a normal effect.",
            "warptext": "Either place a common piece of your color on an empty square, or move 1 of your pieces - combat move if common, standard move if upgraded."
        },
        "Warpmaster": {
            "type": "Etherweave",
            "name": "Warpmaster",
            "text": "You may either return your pending being to your hand or do a standard move with the Warpmaster."
        },
        "Translocationist": {
            "type": "Etherweave",
            "name": "Translocationist",
            "text": "You may swap up to 2 of your heroic pieces with your common pieces.",
            "warptext": "Gain an action."
        },
        "Lesser Shadow Twin": {
            "type": "Etherweave",
            "name": "Lesser Shadow Twin",
            "text": "If Greater Shadow Twin is in your discard pile, choose one of your pieces and destroy up to 2 common pieces adjacent to it.",
            "warptext": "Upgrade 1 of your common pieces."
        }
    },
    "task": {
        "Red Legends": {
            "type": "task",
            "name": "Red Legends",
            "text": "You have at least 2 upgraded pieces on red squares, and at least 1 of them is legendary."
        },
        "Imprisonment": {
            "type": "task",
            "name": "Imprisonment",
            "text": "You have at least 6 pieces adjacent to the same enemy piece."
        },
        "Green Legends": {
            "type": "task",
            "name": "Green Legends",
            "text": "You have at least 2 upgraded pieces on green squares, and at least 1 of them is legendary."
        },
        "Rainbow Dominance": {
            "name": "Rainbow Dominance",
            "type": "task",
            "text": "You have more upgraded pieces on red squares and more upgraded pieces on green squares than your opponent does."
        },
        "Green Summoning": {
            "type": "task",
            "name": "Green Summoning",
            "text": "You summoned at least 2 beings this turn, at least 1 on a green square."
        },
        "Red Summoning": {
            "type": "task",
            "name": "Red Summoning",
            "text": "You summoned at least 2 beings this turn, at least 1 on a red square."
        },
        "Devastation": {
            "name": "Devastation",
            "type": "task",
            "text": "You destroyed at least 4 enemy pieces this turn."
        },
        "Envelopment": {
            "type": "task",
            "name": "Envelopment",
            "text": "You have at least 7 pieces adjacent to the same enemy piece."
        },
        "Red Conquest": {
            "name": "Red Conquest",
            "type": "task",
            "text": "You have at least 3 pieces on red squares, and at least 2 of them are upgraded."
        },
        "Central Dominance": {
            "type": "task",
            "name": "Central Dominance",
            "text": "You have at least 5 pieces on the nine central squares, and at least 2 of them are upgraded."
        },
        "Green Conquest": {
            "name": "Green Conquest",
            "type": "task",
            "text": "You have at least 3 pieces on green squares, and at least 2 of them are upgraded."
        },
        "Heroic Devastation": {
            "type": "task",
            "name": "Heroic Devastation",
            "text": "You destroyed at least 4 enemy pieces this turn, at least 2 of them upgraded."
        },
        "End of Legends": {
            "type": "task",
            "name": "End of Legends",
            "text": "You destroyed at least 1 legendary enemy piece or 2 heroic enemy pieces this turn."
        },
        "Color Conquest": {
            "type": "task",
            "name": "Color Conquest",
            "text": "You have at least 5 pieces on red and/or green squares, and at least 3 of them are upgraded."
        },
        "Line Dominance": {
            "type": "task",
            "name": "Line Dominance",
            "text": "On one of the orthogonal lines through the central squares, you have 6 more pieces than your opponent does."
        },
        "Center Cross": {
            "name": "Center Cross",
            "type": "task",
            "text": "You have at least 5 pieces on the central squares in a + or x pattern."
        },
        "Legendary Summoning": {
            "type": "task",
            "name": "Legendary Summoning",
            "text": "You summoned at least 2 beings this turn, at least one of them legendary."
        },
        "Isolation": {
            "type": "task",
            "name": "Isolation",
            "text": "An enemy piece is within 2 squares of another enemy piece, but it cannot get adjacent to any enemy piece in 3 or fewer moves through empty squares."
        },
        "Heroic Destruction": {
            "type": "task",
            "name": "Heroic Destruction",
            "text": "You destroyed at least 3 enemy pieces this turn, at least 1 of them upgraded."
        },
        "Diagonals": {
            "type": "task",
            "name": "Diagonals",
            "text": "You have at least 4 pieces on each diagonal, and at least 1 of your pieces on each diagonal is upgraded."
        },
        "Corner Chain": {
            "name": "Corner Chain",
            "type": "task",
            "text": "Squares in two opposite corners of the board are connected by a chain of your pieces."
        },
        "Destruction": {
            "type": "task",
            "name": "Destruction",
            "text": "You destroyed at least 3 enemy pieces this turn."
        },
        "Side Chain": {
            "type": "task",
            "name": "Side Chain",
            "text": "Squares on two opposite sides of the board are connected by a chain of your pieces."
        },
        "Colored Summoning": {
            "type": "task",
            "name": "Colored Summoning",
            "text": "You summoned at least 2 beings on red and/or green squares this turn. (Both of them may have been summoned on the same square.)"
        }
    },
    "Flare": {
        3: {
            "type": "Flare",
            "upgraded": "Place 1 common piece of your color on any empty square.",
            "pieces": "Place 1 common piece of your color on any empty square, or convert 1 common enemy piece to your color."
        },
        9: {
            "type": "Flare",
            "upgraded": "Place 2 common pieces of your color on empty squares.",
            "pieces": "Place 1 common piece of your color on any empty square."
        },
        8: {
            "type": "Flare",
            "upgraded": "Place 1 heroic piece of your color on any empty square.",
            "pieces": "You may do 1 standard move and 1 combat move (in either order), using your common pieces."
        },
        6: {
            "type": "Flare",
            "upgraded": "Place 1 common piece of your color on any empty square.",
            "pieces": "Upgrade 1 of your common pieces. Gain an action."
        },
        4: {
            "type": "Flare",
            "upgraded": "Do 1 standard move with one of your common pieces, or upgrade 1 of your common pieces.",
            "pieces": "Place 2 common pieces of your color on empty squares."
        },
        2: {
            "type": "Flare",
            "upgraded": "You may do up to 3 standard moves, using your common pieces.",
            "pieces": "Gain an action."
        },
        0: {
            "type": "Flare",
            "upgraded": "Place 1 common piece of your color on any empty square.",
            "pieces": "Place 1 heroic piece of your color on any empty square."
        },
        5: {
            "type": "Flare",
            "upgraded": "Place 1 common piece of your color on any empty square, or upgrade 1 of your common pieces.",
            "pieces": "You may do 1 combat leap with one of your common pieces."
        },
        11: {
            "type": "Flare",
            "upgraded": "You may do 1 standard leap with one of your common pieces.",
            "pieces": "Gain an action."
        },
        7: {
            "type": "Flare",
            "upgraded": "Gain an action.",
            "pieces": "Place 1 common piece of your color on any empty square."
        },
        10: {
            "type": "Flare",
            "upgraded": "Place 1 common piece of your color on any empty square.",
            "pieces": "You may do 1 combat move or 2 standard moves, using your non-legendary pieces."
        },
        1: {
            "type": "Flare",
            "upgraded": "Place 1 common piece of your color on any empty square.",
            "pieces": "Place 1 common piece of your color on any empty square."
        }
    },
    "Legends": {
        "The Eldest Tree": {
            "type": "Legends",
            "name": "The Eldest Tree",
            "text": "On up to 3 adjacent squares: if it has an enemy non-legendary piece, destroy it; if it has your common piece, upgrade it; if it is empty, place 1 common piece of your color there."
        },
        "Fire Dragon": {
            "type": "Legends",
            "name": "Fire Dragon",
            "text": "Choose one of the indicated directions: Destroy all non-legendary pieces up to distance 2 in that direction and in both directions at 45 degrees to it."
        },
        "Two-Headed Dragon": {
            "type": "Legends",
            "name": "Two-Headed Dragon",
            "text": "You may upgrade 1 of the pieces used to summon the Two-Headed Dragon. If you do, you may destroy 1 heroic piece adjacent to the upgraded piece."
        },
        "Earth Elemental": {
            "type": "Legends",
            "name": "Earth Elemental",
            "text": "Destroy a non-legendary piece on or adjacent to a red square. Then upgrade a common piece on or adjacent to a green square. Then the Earth Elemental may do 1 combat move to an adjacent red or green square."
        },
        "Titan": {
            "type": "Legends",
            "name": "Titan",
            "text": "Destroy all orthogonally adjacent pieces and all non-legendary diagonally adjacent pieces. They do not count as pieces destroyed by you."
        },
        "Angel of Death": {
            "type": "Legends",
            "name": "Angel of Death",
            "text": "You may choose any 1 piece other than the Angel of Death: Upgrade it and then do a combat leap onto its square with the Angel of Death."
        },
        "Hell Bull": {
            "type": "Legends",
            "name": "Hell Bull",
            "text": "Choose any direction: The Hell Bull may do any number of combat moves in that direction. If it destroys a legendary piece, it stops."
        },
        "Storm Elemental": {
            "type": "Legends",
            "name": "Storm Elemental",
            "text": "You may place 1 piece of your color on an empty square up to distance 3. With it, do up to 1 (if legendary), 3 (if heroic), or 5 (if common) combat moves in one direction. Then destroy it."
        },
        "Fire Elemental": {
            "type": "Legends",
            "name": "Fire Elemental",
            "text": "Destroy either all non-legendary enemy pieces on all adjacent squares or all common enemy pieces up to distance 2."
        },
        "Time Elemental": {
            "type": "Legends",
            "name": "Time Elemental",
            "text": "After this turn, take an extra turn (even if the end of the game has been triggered)."
        },
        "Bone Catapult": {
            "type": "Legends",
            "name": "Bone Catapult",
            "text": "You may choose any 1 piece in any of the indicated directions: Destroy it and all common pieces adjacent to it."
        },
        "Leviathan": {
            "type": "Legends",
            "name": "Leviathan",
            "text": "Chose one: Either downgrade a connected group of up to 3 upgraded pieces or destroy a connected group of up to 4 common pieces. (A group may have multiple colors.)"
        }
    },
}
all_fetched_metadata[Faction.SOUTHERN.value] = all_fetched_metadata.get(Faction.IMPERIAL.value)
all_fetched_metadata[Faction.NORTHERN.value] = all_fetched_metadata.get(Faction.IMPERIAL.value)
