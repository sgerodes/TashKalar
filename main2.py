from imageManager import ImageManager
from models import Faction, NonFactionType


if __name__ == '__main__':
    ImageManager.create_singles_for_card_type(NonFactionType.FLARE.value)
    # all_faction_images = ImageManager.create_all_cards_for(NonFactionType.TASK.value)
    # print(all_faction_images)
