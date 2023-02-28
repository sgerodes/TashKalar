import os
import json
import constants
import logging
from metadata import all_manual_metadata_ordered, all_fetched_metadata
from models import *
# from imageManager import ImageManager
import imageManager
import metadataManager


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

get_manual_metadata_for_card = metadataManager.MetadataManager.get_manual_metadata_for_card
get_fetched_metadata_for_card = metadataManager.MetadataManager.get_fetched_metadata_for_card


def create_new_folder(folder_name):
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, folder_name)
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)


def create_card(card_type: str, card_name: str) -> Card:
    if card_type in constants.factions_all:
        card = CreatureCard()
        card.name = card_name
        card.text = get_fetched_metadata_for_card(card_type, card_name).get('text')
        card.common_cost = get_manual_metadata_for_card(card_type, card_name).get('common_cost')

    elif card_type == NonFactionType.LEGEND.value:
        card = LegendaryCard()
        card.name = card_name
        card.text = get_fetched_metadata_for_card(card_type, card_name).get('text')
        card.common_cost = get_manual_metadata_for_card(card_type, card_name).get('common_cost')
        card.upgraded_cost = get_manual_metadata_for_card(card_type, card_name).get('upgraded_cost')

    elif card_type == NonFactionType.TASK.value:
        card = TaskCard()
        card.name = card_name
        card.text = get_fetched_metadata_for_card(card_type, card_name).get('text')
        card.points = get_manual_metadata_for_card(card_type, card_name).get('points')

    elif card_type == NonFactionType.FLARE.value:
        card = FlareCard()
        card.upgraded_text = get_fetched_metadata_for_card(card_type, card_name).get('upgraded')
        card.pieces_text = get_fetched_metadata_for_card(card_type, card_name).get('pieces')
        card.upgraded_cost = get_manual_metadata_for_card(card_type, card_name).get('upgraded_cost')
        card.pieces_cost = get_manual_metadata_for_card(card_type, card_name).get('pieces_cost')

    else:
        logger.warning(f'Type {card_type} is not known')
        raise RuntimeError()

    card.card_type = card_type
    if card_type == NonFactionType.FLARE.value:
        card.big_image_index = metadataManager.MetadataManager.get_index_in_big_image_for_card(card_type, card_name)
    else:
        card.big_image_index = card_name
    card.pilImage = imageManager.ImageManager.get_card_image_from_big_image(card_type, card_name)

    return card
