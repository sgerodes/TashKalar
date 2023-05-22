from PIL import Image
import constants
from metadata import all_manual_metadata_ordered
import models
import logging
import typing as t
import utils
from functools import reduce
from metadataManager import MetadataManager
from collections import defaultdict


logger = logging.getLogger()


class ImageManager:
    ranked_pictures = {}

    @staticmethod
    def concat_images_h(im1, im2):  # TODO test
        dst = Image.new('RGB', (im1.width + im2.width, max(im1.height, im2.height)))
        dst.paste(im2, (0, 0))
        dst.paste(im1, (im2.width, 0))
        return dst

    @staticmethod
    def concat_images_v(im1, im2):  # TODO test
        dst = Image.new('RGB', (max(im1.width, im2.width), im1.height + im2.height))
        dst.paste(im1, (0, 0))
        dst.paste(im2, (0, im1.height))
        return dst

    @staticmethod
    def grey_out(image: Image.Image, how=None):
        if how is None or how == 'full':
            return image.convert('LA')
        elif how == 'top_half':
            width, height = image.size
            top_half = ImageManager.grey_out(image.crop((0, 0, width, height / 2)))
            bottom_half = image.crop((0, height / 2, width, height))
            return ImageManager.concat_images_v(top_half, bottom_half)
        elif how == 'bottom_half':
            width, height = image.size
            top_half = image.crop((0, 0, width, height / 2))
            bottom_half = ImageManager.grey_out(image.crop((0, height / 2, width, height)))
            return ImageManager.concat_images_v(top_half, bottom_half)

    @staticmethod
    def get_card_width(card_type):
        if card_type == models.NonFactionType.TASK.value:
            return models.TaskCard.image_width
        else:
            return models.CreatureCard.image_width

    @staticmethod
    def create_all_cards_for(card_type: str) -> t.List[models.Card]:
        return [utils.create_card(card_type, manual_metadata['name'])
                for manual_metadata in all_manual_metadata_ordered[card_type]]



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
        pil_images = [Image.open(f'{constants.pictures_folder}/{fac}_big.webp')
                      for fac in constants.factions_imperial_combined]
        combined_image = reduce(ImageManager.concat_images_v, pil_images)
        combined_image.save(f'{constants.combined_pictures_path}/combined.webp')

    @staticmethod
    def create_singles_for_card_type(card_type):
        folder = f'{constants.singles_folder_path}/{card_type}'
        utils.create_new_folder(folder)
        all_type_cards = ImageManager.create_all_cards_for(card_type)
        for card in all_type_cards:
            if card_type == models.NonFactionType.FLARE.value:
                card_path = f'{folder}/{card.big_image_index}.webp'
            else:
                card_path = f'{folder}/{card.name}.webp'
            logger.info(f'saving {card_path}')
            card.pilImage.save(card_path)

    @staticmethod
    def create_all_singles():
        for card_type in constants.card_types_all:
            ImageManager.create_singles_for_card_type(card_type)

    @staticmethod
    def create_ranked_picture_for_card_type(card_type,
                                            cost_rank_provider=None,
                                            ranked_image_infix='',
                                            image_altering_provider=None):
        if not cost_rank_provider:
            cost_rank_provider = lambda card: card.common_cost

        cost_to_cards = defaultdict(list)
        for card in ImageManager.create_all_cards_for(card_type):
            img = card.pilImage if not image_altering_provider else image_altering_provider(card.pilImage)
            cost_to_cards[cost_rank_provider(card)].append(img)

        image_rows = [reduce(ImageManager.concat_images_h, cost_to_cards[cost])
                      for cost in sorted(cost_to_cards.keys())]
        ranked_image = reduce(ImageManager.concat_images_v, image_rows)
        ranked_image.save(f'{constants.ranked_pictures_path}/{card_type}{ranked_image_infix}_ranked.webp')
        ImageManager.ranked_pictures[card_type + ranked_image_infix] = ranked_image

    @staticmethod
    def create_legendary_ranked_pictures():
        card_type = models.NonFactionType.LEGEND.value
        create_ranked = ImageManager.create_ranked_picture_for_card_type
        create_ranked(card_type=card_type,
                      cost_rank_provider=lambda card: card.common_cost,
                      ranked_image_infix="_common")
        create_ranked(card_type=card_type,
                      cost_rank_provider=lambda card: card.upgraded_cost,
                      ranked_image_infix="_upgraded")
        create_ranked(card_type=card_type,
                      cost_rank_provider=lambda card: card.get_total_cost(),
                      ranked_image_infix="_total")
        upgraded_cost_weight = 3
        create_ranked(card_type=card_type,
                      cost_rank_provider=lambda card: card.common_cost + card.upgraded_cost * upgraded_cost_weight,
                      ranked_image_infix=f"_total_weighted_x{upgraded_cost_weight}")


    @staticmethod
    def create_flare_ranked_pictures():
        card_type = models.NonFactionType.FLARE.value
        create_ranked = ImageManager.create_ranked_picture_for_card_type
        create_ranked(card_type=card_type,
                      cost_rank_provider=lambda card: card.pieces_cost,
                      ranked_image_infix="_pieces")
                      #image_altering_provider=lambda image: ImageManager.grey_out(image, how='top_half'))
        create_ranked(card_type=card_type,
                      cost_rank_provider=lambda card: card.upgraded_cost,
                      ranked_image_infix="_upgraded")
                      #image_altering_provider=lambda image: ImageManager.grey_out(image, how='bottom_half'))

    @staticmethod
    def create_ranked_pictures(create_combined=False):
        for card_type in constants.factions_imperial_combined:
            ImageManager.create_ranked_picture_for_card_type(card_type)

        if create_combined:
            # crate combined ranked picture
            ranked_images_list = [ImageManager.ranked_pictures[card_type]
                                  for card_type in constants.factions_imperial_combined
                                  if card_type in ImageManager.ranked_pictures]
            combined_ranked_image = reduce(ImageManager.concat_images_v, ranked_images_list)
            combined_ranked_image.save(f'{constants.ranked_pictures_path}/ranked_combined.webp')
