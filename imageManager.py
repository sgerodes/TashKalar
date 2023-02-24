from PIL import Image
import constants
from metadata import all_manual_metadata_ordered
import models


def init_image_indexes():
    image_indexes = dict()
    for card_type, type_cards_list in all_manual_metadata_ordered.items():
        image_indexes[card_type] = dict()
        for i, metadata in enumerate(type_cards_list):
            image_indexes[card_type][metadata.get('name')] = i
    return image_indexes


class ImageManager:
    image_indexes = init_image_indexes()

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
    def get_card_image_from_big_image(card_type: str, card_name: str):
        big_pil_image = Image.open(f'{constants.pictures_folder}/{card_type}_big.webp')
        card_order_number = ImageManager.image_indexes[card_type][card_name]
        card_width = ImageManager.get_card_width(card_type)
        height = big_pil_image.height
        return big_pil_image.crop((card_width * card_order_number, 0, card_width * (card_order_number + 1), height))

    @staticmethod
    def create_combined_picture():
        create_new_folder(combined_pictures_path)
        pil_images = [Image.open(f'{pictures_folder}/{f.value}_big.webp') for f in factions_imperial_combined]
        combined_image = reduce(concat_images_v, pil_images)
        combined_image.save(f'{combined_pictures_path}/combined.webp')

    @staticmethod
    def get_card_image_from_big_image(faction: str, card_name: str):
        cards_order = cards_pictures_order[faction]
        big_pil_image = Image.open(f'{pictures_folder}/{faction}_big.webp')
        card_order_number = cards_order.index(card_name)

        card_width = 250
        height = big_pil_image.height
        return big_pil_image.crop((card_width * card_order_number, 0, card_width * (card_order_number + 1), height))
