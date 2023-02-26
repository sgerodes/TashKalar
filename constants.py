from models import Faction, NonFactionType

tasks_count = 24
faction_card_count = 18
legend_count = 12
flares_count = 12

pictures_folder = 'resources/pictures'
ranked_pictures_path = f'{pictures_folder}/ranked'
combined_pictures_path = f'{pictures_folder}/combined'
description_folder = 'resources/descriptions'
singles_folder_path = f"{pictures_folder}/single_cards"
all_in_one_fetched_metadata_path = f'{description_folder}/all_in_one.json'

factions_original = tuple(map(lambda e: e.value, (Faction.SYLVAN, Faction.SOUTHERN, Faction.NORTHERN, Faction.HIGHLAND,
                     Faction.EVERFROST, Faction.NETHERVOID, Faction.ETHERWEAVE)))
factions_imperial_combined = tuple(map(lambda e: e.value, (Faction.SYLVAN, Faction.IMPERIAL, Faction.HIGHLAND,
                              Faction.EVERFROST, Faction.NETHERVOID, Faction.ETHERWEAVE)))
factions_all = tuple(map(lambda e: e.value, (Faction.SYLVAN,  Faction.SOUTHERN, Faction.NORTHERN, Faction.IMPERIAL, Faction.HIGHLAND,
                              Faction.EVERFROST, Faction.NETHERVOID, Faction.ETHERWEAVE)))
imperial_factions = tuple(map(lambda e: e.value, {Faction.SOUTHERN, Faction.NORTHERN, Faction.IMPERIAL}))
non_faction_card = tuple(map(lambda e: e.value, (NonFactionType.TASK, NonFactionType.FLARE, NonFactionType.LEGEND)))
card_types_all = factions_all + non_faction_card
