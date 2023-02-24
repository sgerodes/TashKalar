import os
import json
import constants
import logging
from metadata import all_manual_metadata_ordered
from models import *


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


with open(constants.all_in_one_fetched_metadata_path, 'r') as f:
    all_fetched_metadata = json.loads(f.read())


def create_new_folder(folder_name):
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, folder_name)
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)


def create_card(card_type: str, card_name: str) -> Card:
    fetched_metadata = all_fetched_metadata[card_type]
    manual_metadata = all_manual_metadata_ordered[card_type]

    if card_type in constants.factions_all:
        card = CreatureCard()
        card.name = card_name
        card.text = fetched_metadata.get(card_name).get('text')
        # TODO
    elif type == NonFactionType.LEGEND.value:
        card = LegendaryCard()
        card.name = card_name
        card.text = fetched_metadata.get(card_name).get('text')
        # TODO
    elif type == NonFactionType.TASK.value:
        card = TaskCard()
        # TODO
    elif type == NonFactionType.FLARE.value:
        card = FlareCard()
        # TODO
    else:
        logger.warning(f'Type {type} is not known')
        raise RuntimeError()

    # card.pilImage = get_card_image_from_big_image(faction, card_name)

