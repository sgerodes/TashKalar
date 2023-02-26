from imageManager import ImageManager
from models import Faction, NonFactionType


if __name__ == '__main__':
    ImageManager.create_ranked_pictures()
    # all_faction_images = ImageManager.create_all_cards_for(NonFactionType.TASK.value)
    # print(all_faction_images)
