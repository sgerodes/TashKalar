from imageManager import ImageManager
from models import Faction, NonFactionType
import utils
import constants
from statistics import mean


if __name__ == '__main__':
    averages = dict()
    for card_type in constants.factions_imperial_combined:
        all_cards_for_card_type = ImageManager.create_all_cards_for(card_type)
        averages[card_type] = mean(map(lambda card: card.common_cost, all_cards_for_card_type))

    for av in sorted(list(averages.items()), key=lambda c: c[1]):
        print(av)

    # ImageManager.create_legendary_ranked_pictures()
    # all_faction_images = ImageManager.create_all_cards_for(NonFactionType.TASK.value)
    # print(all_faction_images)
