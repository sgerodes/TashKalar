from PIL import Image
import constants
from metadata import all_manual_metadata_ordered
import models
import logging
import typing as t
import utils
from functools import reduce
from metadataManager import MetadataManager


logger = logging.getLogger()


class ImageManager:
    @staticmethod
    def concat_images_h(im1, im2):  # TODO test
        dst = Image.new('RGB', (im1.width + im2.width, max(im1.height, im2.height)))
        dst.paste(im2, (0, 0))
        dst.paste(im1, (im2.width, 0))
        return dst

    @staticmethod
    def concat_images_v(im1, im2):  # TODO test
        dst = Image.new('RGB', (max(im1.width, im2.width), im1.height + im2.height))
        dst.paste(im2, (0, 0))
        dst.paste(im1, (0, im2.height))
        return dst

    @staticmethod
    def get_card_width(card_type):
        if card_type == models.NonFactionType.TASK.value:
            return models.FlareCard.image_width
        else:
            return models.CreatureCard.image_width

    @staticmethod
    def create_all_cards_for(card_type: str) -> t.List[models.Card]:
        return [utils.create_card(card_type, manual_metadata['name'])
                for manual_metadata in all_manual_metadata_ordered[card_type]]

    @staticmethod
    def create_singles():
        pass


    @staticmethod
    def get_card_image_from_big_image(card_type: str, card_name: str) -> t.Optional[Image.Image]:
        big_pil_image = Image.open(f'{constants.pictures_folder}/{card_type}_big.webp')
        if MetadataManager.get_index_in_big_image_for_card(card_type, card_name) is None:
            logger.warning(f'For {card_type}:{card_name} there is no configuration for the image')
            return None
        card_order_number = MetadataManager.get_index_in_big_image_for_card(card_type, card_name)
        card_width = ImageManager.get_card_width(card_type)
        height = big_pil_image.height
        return big_pil_image.crop((card_width * card_order_number, 0, card_width * (card_order_number + 1), height))

    @staticmethod
    def create_combined_picture():
        pil_images = [Image.open(f'{constants.pictures_folder}/{f.value}_big.webp')
                      for f in constants.factions_imperial_combined]
        combined_image = reduce(ImageManager.concat_images_v, pil_images)
        combined_image.save(f'{constants.combined_pictures_path}/combined.webp')
