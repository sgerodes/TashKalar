from imageManager import ImageManager
from models import Faction, NonFactionType
import utils
import constants
from statistics import mean


def print_averages():
    averages = dict()
    for card_type in constants.factions_imperial_combined:
        all_cards_for_card_type = ImageManager.create_all_cards_for(card_type)
        averages[card_type] = mean(map(lambda card: card.common_cost, all_cards_for_card_type))

    for av in sorted(list(averages.items()), key=lambda c: c[1]):
        print(av)


if __name__ == '__main__':
    ImageManager.create_flare_ranked_pictures()

